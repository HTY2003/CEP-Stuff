Module SCS15

#Region "Enum"
    Const INST_PING As Integer = 1
    Const INST_READ As Integer = 2
    Const INST_WRITE As Integer = 3
    Const INST_REG_WRITE As Integer = 4
    Const INST_ACTION As Integer = 5
    Const INST_RESET As Integer = 6
    Const INST_SYNC_WRITE As Integer = &H83

    Const P_TORQUE_ENABLE As Integer = 40
    Const P_LED As Integer = 41
    Const P_GOAL_POSITION_L As Integer = 42
    Const P_GOAL_POSITION_H As Integer = 43
    Const P_GOAL_TIME_L As Integer = 44
    Const P_GOAL_TIME_H As Integer = 45
    Const P_GOAL_SPEED_L As Integer = 46
    Const P_GOAL_SPEED_H As Integer = 47
    Const P_LOCK As Integer = 48

    Const P_PRESENT_POSITION_L As Integer = 56
    Const P_PRESENT_POSITION_H As Integer = 56
    Const P_PRESENT_SPEED_L As Integer = 56
    Const P_PRESENT_SPEED_H As Integer = 56
    Const P_PRESENT_LOAD_L As Integer = 60
    Const P_PRESENT_LOAD_H As Integer = 61
    Const P_PRESENT_VOLTAGE As Integer = 62
    Const P_PRESENT_TEMPERATURE As Integer = 63
    Const P_REGISTERED_INSTRUCTION As Integer = 64
    'Const x As Integer = 65
    Const P_MOVING As Integer = 66
#End Region


    Public Sub SCS15_Set_Position(ByRef SerialPort1 As System.IO.Ports.SerialPort, ID As Integer, Position As Integer, Time As Integer)
        If SerialPort1.IsOpen Then
            Dim B(20) As Byte
            Dim ChkSUm, ndx As Integer
            B(0) = &HFF : B(1) = &HFF       '<< Start 0xFF 0xFF
            B(2) = ID                       '<< ID
            B(3) = 9                        '<< Length
            B(4) = INST_WRITE               '<< Instruction
            B(5) = P_GOAL_POSITION_L
            Dim bytes As Byte() = BitConverter.GetBytes(Position)
            B(6) = bytes(1) '1 upper 'Position \ 256
            B(7) = bytes(0) '0 lower 'Position Mod 256
            bytes = BitConverter.GetBytes(Time)
            B(8) = bytes(1) '1 upper 'Time \ 256
            B(9) = bytes(0) '0 lower 'Time Mod 256
            B(10) = 0 'Speed
            B(11) = 0 'Speed
            ChkSUm = 0 '(B(2) + B(3) + B(4) + B(5) + B(6) + B(7) + B(8) + B(9) + B(10) + B(11)) Mod 256
            For ndx = 2 To 11
                ChkSUm = ChkSUm + B(ndx)
            Next
            B(12) = CByte((Not (ChkSUm)) And &HFF)
            SerialPort1.Write(B, 0, 13)
        End If
    End Sub

    Public Function SCS15_Get_Position(ByRef SerialPort1 As System.IO.Ports.SerialPort, ID As Integer) As Integer
        Dim Position As Integer = -1

        'Instruction Packet：0XFF 0XFF 0X01 0X04 0X02 0X38 0X02 0XBE
        If SerialPort1.IsOpen Then
            FMain.GRxMode = 0
Again:
            Dim B(20) As Byte
            Dim ChkSUm, ndx As Integer
            B(0) = &HFF : B(1) = &HFF       '<< Start 0xFF 0xFF
            B(2) = ID                       '<< ID
            B(3) = 4                        '<< Length
            B(4) = INST_READ                '<< Instruction
            B(5) = P_PRESENT_POSITION_L
            B(6) = 2                        '<< Read 2 bytes
            ChkSUm = 0 '(B(2) + B(3) + B(4) + B(5) + B(6) + B(7) + B(8) + B(9) + B(10) + B(11)) Mod 256
            For ndx = 2 To 6
                ChkSUm = ChkSUm + B(ndx)
            Next
            B(7) = CByte((Not (ChkSUm)) And &HFF)
            SerialPort1.Write(B, 0, 8)

            DelayMS(10)

            'Rx 
            '### TODO :: TIME OUT #####
            Dim D1, D2 As Integer
            Dim D1Num, DLen, DCRC As Integer
            Dim Str As String = ""
            Const DMax As Long = 10000
            '0XFF 0XFF 0X01 0X03 0X00 0X20 OXDA
            Dim TOut As Long = 0
            '1st byte
            TOut = 0
            Do
                Do
                    D1Num = SerialPort1.BytesToRead()
                    TOut = TOut + 1
                    If TOut > DMax Then
                        GoTo Err
                    End If
                Loop Until D1Num > 0
                D1Num = SerialPort1.Read(B, 0, 1)
                If D1Num > 0 Then
                    Exit Do
                End If
            Loop
            If B(0) <> 255 Then
                GoTo Again
            End If
            '2nd Byte
            TOut = 0
            Do
                Do
                    D1Num = SerialPort1.BytesToRead()
                    If TOut > DMax Then
                        GoTo Err
                    End If
                Loop Until D1Num > 0
                D1Num = SerialPort1.Read(B, 0, 1)
                If D1Num > 0 Then
                    Exit Do
                End If

            Loop
            If B(0) <> 255 Then
                GoTo Again
            End If
            '3rd Byte : ID
            TOut = 0
            Do
                Do
                    D1Num = SerialPort1.BytesToRead()
                Loop Until D1Num > 0
                D1Num = SerialPort1.Read(B, 0, 1)
                If D1Num > 0 Then
                    Exit Do
                End If
                If TOut > DMax Then
                    GoTo Err
                End If
            Loop
            If B(0) <> ID Then
                GoTo Again
            End If
            '4th Byte : length
            TOut = 0
            Do
                Do
                    D1Num = SerialPort1.BytesToRead()
                Loop Until D1Num > 0
                D1Num = SerialPort1.Read(B, 0, 1)
                If D1Num > 0 Then
                    Exit Do
                End If
                If TOut > DMax Then
                    GoTo Err
                End If
            Loop
            DLen = B(0)
            '5th Byte : error
            TOut = 0
            Do
                Do
                    D1Num = SerialPort1.BytesToRead()
                Loop Until D1Num > 0
                D1Num = SerialPort1.Read(B, 0, 1)
                If D1Num > 0 Then
                    Exit Do
                End If
                If TOut > DMax Then
                    GoTo Err
                End If
            Loop
            DLen = B(0)
            '6th Byte : position high
            TOut = 0
            Do
                Do
                    D1Num = SerialPort1.BytesToRead()
                Loop Until D1Num > 0
                D1Num = SerialPort1.Read(B, 0, 1)
                If D1Num > 0 Then
                    Exit Do
                End If
                If TOut > DMax Then
                    GoTo Err
                End If
            Loop
            D1 = B(0)
            '7th Byte : position low
            TOut = 0
            Do
                Do
                    D1Num = SerialPort1.BytesToRead()
                Loop Until D1Num > 0
                D1Num = SerialPort1.Read(B, 0, 1)
                If D1Num > 0 Then
                    Exit Do
                End If
                If TOut > DMax Then
                    GoTo Err
                End If
            Loop
            D2 = B(0)
            '8th Byte : DCRC
            TOut = 0
            Do
                Do
                    D1Num = SerialPort1.BytesToRead()
                Loop Until D1Num > 0
                D1Num = SerialPort1.Read(B, 0, 1)
                If D1Num > 0 Then
                    Exit Do
                End If
                If TOut > DMax Then
                    GoTo Err
                End If
            Loop
            DCRC = B(0)

            Position = D1 * 256 + D2
            FMain.GRxMode = 1

            Return Position
        Else
            FMain.GRxMode = 1
            Return -1
        End If
Err:
        FMain.GRxMode = 1
        Return -1
    End Function





End Module
