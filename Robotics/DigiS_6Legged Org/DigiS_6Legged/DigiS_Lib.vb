Module DigiS_Lib

    Public Structure sServoID
        Public InitPos As Integer
        Public Pos As Integer
    End Structure

    Public Structure sServo
        Public ID() As sServoID
        Public Max As Integer
        Public SerialPort1 As System.IO.Ports.SerialPort

        Public Sub Init(ByVal Num As Integer)
            Max = Num

            ReDim ID(Max)
            Dim i As Integer
            For i = 1 To Max
                ID(i).Pos = -1
                ID(i).InitPos = -1
            Next
        End Sub

        Public Sub Init_AllPosition()
            Dim i As Integer
            For i = 1 To Max
                ID(i).Pos = ID(i).InitPos
            Next
        End Sub

        Public Sub SetAllPos2Init(ByVal Duration As Integer)
            Dim i, Pos, T As Integer
            T = Duration
            If T < 100 Then T = 100
            For i = 1 To Servo.Max
                Try
                    Pos = Servo.ID(i).InitPos
                    If Pos >= 0 Then
                        SCS15_Set_Position(SerialPort1, i, Pos, T)
                    End If
                Catch ex As Exception
                End Try
                DelayMS(1)
            Next
            DelayMS(T)
        End Sub

        Public Sub SetAllPos(ByVal Duration As Integer)
            Dim i, Pos, T As Integer
            T = Duration
            If T < 100 Then T = 100
            For i = 1 To Servo.Max
                Try
                    Pos = Servo.ID(i).Pos
                    If Pos >= 0 Then
                        SCS15_Set_Position(SerialPort1, i, Pos, T)
                    End If
                Catch ex As Exception
                    MsgBox("err")
                End Try
                DelayMS(1)
            Next
            DelayMS(T)
        End Sub


        Public Sub SetPos(ByVal Pos1 As Integer)
            Servo.ID(1).Pos = Pos1
        End Sub
        Public Sub SetPos(ByVal Pos1 As Integer, ByVal Pos2 As Integer)
            Servo.ID(1).Pos = Pos1 : Servo.ID(2).Pos = Pos2
        End Sub
        Public Sub SetPos(ByVal Pos1 As Integer, ByVal Pos2 As Integer, ByVal Pos3 As Integer)
            Servo.ID(1).Pos = Pos1 : Servo.ID(2).Pos = Pos2 : Servo.ID(3).Pos = Pos3
        End Sub

        Public Sub Position(ByVal Pos1 As Integer, Optional ByVal Pos2 As Integer = -1, Optional ByVal Pos3 As Integer = -1, Optional ByVal Pos4 As Integer = -1, Optional ByVal Pos5 As Integer = -1, _
                            Optional ByVal Pos6 As Integer = -1, Optional ByVal Pos7 As Integer = -1, Optional ByVal Pos8 As Integer = -1, Optional ByVal Pos9 As Integer = -1, Optional ByVal Pos10 As Integer = -1, _
                            Optional ByVal Pos11 As Integer = -1, Optional ByVal Pos12 As Integer = -1, Optional ByVal Pos13 As Integer = -1, Optional ByVal Pos14 As Integer = -1, Optional ByVal Pos15 As Integer = -1, _
                            Optional ByVal Pos16 As Integer = -1, Optional ByVal Pos17 As Integer = -1, Optional ByVal Pos18 As Integer = -1, Optional ByVal Pos19 As Integer = -1, Optional ByVal Pos20 As Integer = -1 _
                            )
            If Pos1 >= 0 Then
                Servo.ID(1).Pos = Pos1
            End If
            If Pos2 >= 0 Then
                Servo.ID(2).Pos = Pos2
            End If
            If Pos3 >= 0 Then
                Servo.ID(3).Pos = Pos3
            End If

            If Pos4 >= 0 Then
                Servo.ID(4).Pos = Pos4
            End If
            If Pos5 >= 0 Then
                Servo.ID(5).Pos = Pos5
            End If
            If Pos6 >= 0 Then
                Servo.ID(6).Pos = Pos6
            End If

            If Pos7 >= 0 Then
                Servo.ID(7).Pos = Pos7
            End If
            If Pos8 >= 0 Then
                Servo.ID(8).Pos = Pos8
            End If
            If Pos9 >= 0 Then
                Servo.ID(9).Pos = Pos9
            End If

            If Pos10 >= 0 Then
                Servo.ID(10).Pos = Pos10
            End If


            If Pos11 >= 0 Then
                Servo.ID(11).Pos = Pos11
            End If
            If Pos12 >= 0 Then
                Servo.ID(12).Pos = Pos12
            End If
            If Pos13 >= 0 Then
                Servo.ID(13).Pos = Pos13
            End If

            If Pos14 >= 0 Then
                Servo.ID(14).Pos = Pos14
            End If
            If Pos15 >= 0 Then
                Servo.ID(15).Pos = Pos15
            End If
            If Pos16 >= 0 Then
                Servo.ID(16).Pos = Pos16
            End If

            If Pos17 >= 0 Then
                Servo.ID(17).Pos = Pos17
            End If
            If Pos18 >= 0 Then
                Servo.ID(18).Pos = Pos18
            End If
            If Pos19 >= 0 Then
                Servo.ID(19).Pos = Pos19
            End If

            If Pos20 >= 0 Then
                Servo.ID(20).Pos = Pos20
            End If
        End Sub


        Public Sub Position_Add(ByVal Pos1 As Integer, Optional ByVal Pos2 As Integer = -1, Optional ByVal Pos3 As Integer = -1, Optional ByVal Pos4 As Integer = -1, Optional ByVal Pos5 As Integer = -1, _
                    Optional ByVal Pos6 As Integer = -1, Optional ByVal Pos7 As Integer = -1, Optional ByVal Pos8 As Integer = -1, Optional ByVal Pos9 As Integer = -1, Optional ByVal Pos10 As Integer = -1, _
                    Optional ByVal Pos11 As Integer = -1, Optional ByVal Pos12 As Integer = -1, Optional ByVal Pos13 As Integer = -1, Optional ByVal Pos14 As Integer = -1, Optional ByVal Pos15 As Integer = -1, _
                    Optional ByVal Pos16 As Integer = -1, Optional ByVal Pos17 As Integer = -1, Optional ByVal Pos18 As Integer = -1, Optional ByVal Pos19 As Integer = -1, Optional ByVal Pos20 As Integer = -1 _
                    )
            If Pos1 >= 0 Then
                Servo.ID(1).Pos = Servo.ID(1).InitPos + Pos1
            End If
            If Pos2 >= 0 Then
                Servo.ID(2).Pos = Servo.ID(2).InitPos + Pos2
            End If
            If Pos3 >= 0 Then
                Servo.ID(3).Pos = Servo.ID(3).InitPos + Pos3
            End If
            If Pos4 >= 0 Then
                Servo.ID(4).Pos = Servo.ID(4).InitPos + Pos4
            End If
            If Pos5 >= 0 Then
                Servo.ID(5).Pos = Servo.ID(5).InitPos + Pos5
            End If
            If Pos6 >= 0 Then
                Servo.ID(6).Pos = Servo.ID(6).InitPos + Pos6
            End If
            If Pos7 >= 0 Then
                Servo.ID(7).Pos = Servo.ID(7).InitPos + Pos7
            End If
            If Pos8 >= 0 Then
                Servo.ID(8).Pos = Servo.ID(8).InitPos + Pos8
            End If
            If Pos9 >= 0 Then
                Servo.ID(9).Pos = Servo.ID(9).InitPos + Pos9
            End If
            If Pos10 >= 0 Then
                Servo.ID(10).Pos = Servo.ID(10).InitPos + Pos10
            End If


            If Pos11 >= 0 Then
                Servo.ID(11).Pos = Servo.ID(11).InitPos + Pos11
            End If
            If Pos12 >= 0 Then
                Servo.ID(12).Pos = Servo.ID(12).InitPos + Pos12
            End If
            If Pos13 >= 0 Then
                Servo.ID(13).Pos = Servo.ID(13).InitPos + Pos13
            End If
            If Pos14 >= 0 Then
                Servo.ID(14).Pos = Servo.ID(14).InitPos + Pos14
            End If
            If Pos15 >= 0 Then
                Servo.ID(15).Pos = Servo.ID(15).InitPos + Pos15
            End If
            If Pos16 >= 0 Then
                Servo.ID(16).Pos = Servo.ID(16).InitPos + Pos16
            End If
            If Pos17 >= 0 Then
                Servo.ID(17).Pos = Servo.ID(17).InitPos + Pos17
            End If
            If Pos18 >= 0 Then
                Servo.ID(18).Pos = Servo.ID(18).InitPos + Pos18
            End If
            If Pos19 >= 0 Then
                Servo.ID(19).Pos = Servo.ID(19).InitPos + Pos19
            End If
            If Pos20 >= 0 Then
                Servo.ID(20).Pos = Servo.ID(20).InitPos + Pos20
            End If
        End Sub




        'Public Sub Position_L2(ByVal Pos As Integer)
        '    'Servo.ID(1).Pos = Servo.ID(1).InitPos
        '    'Servo.ID(2).Pos = Servo.ID(2).InitPos
        '    'Servo.ID(3).Pos = Servo.ID(3).InitPos
        '    'Servo.ID(4).Pos = Servo.ID(4).InitPos
        '    'Servo.ID(5).Pos = Servo.ID(5).InitPos
        '    'Servo.ID(6).Pos = Servo.ID(6).InitPos
        '    'Servo.ID(7).Pos = Servo.ID(7).InitPos
        '    'Servo.ID(8).Pos = Servo.ID(8).InitPos
        '    'Servo.ID(9).Pos = Servo.ID(9).InitPos
        '    'Servo.ID(10).Pos = Servo.ID(10).InitPos
        '    'Servo.ID(11).Pos = Servo.ID(11).InitPos
        '    'Servo.ID(12).Pos = Servo.ID(12).InitPos
        '    'Servo.ID(13).Pos = Servo.ID(13).InitPos
        '    'Servo.ID(14).Pos = Servo.ID(14).InitPos
        '    'Servo.ID(15).Pos = Servo.ID(15).InitPos
        '    'Servo.ID(16).Pos = Servo.ID(16).InitPos
        '    'Servo.ID(17).Pos = Servo.ID(17).InitPos
        '    'Servo.ID(18).Pos = Servo.ID(18).InitPos
        '    'Servo.ID(19).Pos = Servo.ID(19).InitPos
        '    'Servo.ID(20).Pos = Servo.ID(20).InitPos



        '    Servo.ID(2).Pos = Servo.ID(2).InitPos + Pos
        '    Servo.ID(5).Pos = Servo.ID(5).InitPos + Pos
        '    Servo.ID(8).Pos = Servo.ID(8).InitPos + Pos

        '    Servo.ID(12).Pos = Servo.ID(12).InitPos - Pos
        '    Servo.ID(15).Pos = Servo.ID(15).InitPos - Pos
        '    Servo.ID(18).Pos = Servo.ID(18).InitPos - Pos

        'End Sub
        'Public Sub Position_L3(ByVal Pos As Integer)
        '    Servo.ID(3).Pos = Servo.ID(3).InitPos + Pos
        '    Servo.ID(6).Pos = Servo.ID(6).InitPos + Pos
        '    Servo.ID(9).Pos = Servo.ID(9).InitPos + Pos

        '    Servo.ID(13).Pos = Servo.ID(13).InitPos - Pos
        '    Servo.ID(16).Pos = Servo.ID(16).InitPos - Pos
        '    Servo.ID(19).Pos = Servo.ID(19).InitPos - Pos
        'End Sub



        'Public Sub Position_Alt_RightL(ByVal Pos As Integer)
        '    Servo.ID(2).Pos = Servo.ID(2).InitPos + Pos
        '    'Servo.ID(5).Pos = Servo.ID(5).InitPos + Pos
        '    Servo.ID(8).Pos = Servo.ID(8).InitPos + Pos

        '    'Servo.ID(12).Pos = Servo.ID(12).InitPos - Pos
        '    Servo.ID(15).Pos = Servo.ID(15).InitPos - Pos
        '    'Servo.ID(18).Pos = Servo.ID(18).InitPos - Pos
        'End Sub
        'Public Sub Position_Alt_LeftL(ByVal Pos As Integer)
        '    'Servo.ID(2).Pos = Servo.ID(2).InitPos + Pos
        '    Servo.ID(5).Pos = Servo.ID(5).InitPos + Pos
        '    'Servo.ID(8).Pos = Servo.ID(8).InitPos + Pos

        '    Servo.ID(12).Pos = Servo.ID(12).InitPos - Pos
        '    'Servo.ID(15).Pos = Servo.ID(15).InitPos - Pos
        '    Servo.ID(18).Pos = Servo.ID(18).InitPos - Pos
        'End Sub



        ''forward
        'Public Sub Position_Alt_Move_Forward_S1(ByVal Pos As Integer)
        '    Servo.Position_Alt_RightL(-150) 'UP

        '    Servo.ID(1).Pos = Servo.ID(1).InitPos - Pos
        '    Servo.ID(7).Pos = Servo.ID(7).InitPos - Pos
        '    Servo.ID(14).Pos = Servo.ID(14).InitPos - Pos

        '    Servo.ID(4).Pos = Servo.ID(4).InitPos + Pos
        '    Servo.ID(11).Pos = Servo.ID(11).InitPos + Pos
        '    Servo.ID(17).Pos = Servo.ID(17).InitPos + Pos
        'End Sub
        'Public Sub Position_Alt_Move_Forward_S2(ByVal Pos As Integer)
        '    Servo.Position_Alt_LeftL(-150) 'UP

        '    Servo.ID(1).Pos = Servo.ID(1).InitPos + Pos
        '    Servo.ID(7).Pos = Servo.ID(7).InitPos + Pos
        '    Servo.ID(14).Pos = Servo.ID(14).InitPos + Pos

        '    Servo.ID(4).Pos = Servo.ID(4).InitPos - Pos
        '    Servo.ID(11).Pos = Servo.ID(11).InitPos - Pos
        '    Servo.ID(17).Pos = Servo.ID(17).InitPos - Pos
        'End Sub












        'Public Sub Position_Alt_Move_Forward_S3(ByVal Pos As Integer)
        '    Servo.Position_Alt_RightL(-150) 'UP

        '    Servo.ID(1).Pos = Servo.ID(1).InitPos '+ Pos
        '    Servo.ID(7).Pos = Servo.ID(7).InitPos '+ Pos
        '    Servo.ID(14).Pos = Servo.ID(14).InitPos '+ Pos


        '    'Servo.Position_Alt_LeftL(-150) 'UP

        '    'Servo.ID(1).Pos = Servo.ID(1).InitPos + Pos
        '    'Servo.ID(7).Pos = Servo.ID(7).InitPos + Pos
        '    'Servo.ID(14).Pos = Servo.ID(14).InitPos + Pos
        'End Sub


        'Public Sub Position_Alt_Move_Forward_S4(ByVal Pos As Integer)
        '    'Servo.Position_Alt_RightL(-150) 'UP

        '    'Servo.ID(1).Pos = Servo.ID(1).InitPos '+ Pos
        '    'Servo.ID(7).Pos = Servo.ID(7).InitPos '+ Pos
        '    'Servo.ID(14).Pos = Servo.ID(14).InitPos '+ Pos

        'End Sub




        Public Sub Position_Ndx(ByVal Ndx As Integer,
                    ByVal Pos1 As Integer, Optional ByVal Pos2 As Integer = -1, Optional ByVal Pos3 As Integer = -1, Optional ByVal Pos4 As Integer = -1, Optional ByVal Pos5 As Integer = -1,
                    Optional ByVal Pos6 As Integer = -1, Optional ByVal Pos7 As Integer = -1, Optional ByVal Pos8 As Integer = -1, Optional ByVal Pos9 As Integer = -1, Optional ByVal Pos10 As Integer = -1
                    )
            If Ndx < 1 Then Exit Sub

            If (Pos1 >= 0) Then
                Servo.ID(Ndx).Pos = Pos1
                If Servo.Max = Ndx Then Exit Sub
            End If
            If (Pos2 >= 0) Then
                Servo.ID(Ndx + 1).Pos = Pos2
                If Servo.Max = (Ndx + 1) Then Exit Sub
            End If
            If (Pos3 >= 0) Then
                Servo.ID(Ndx + 2).Pos = Pos3
                If Servo.Max = (Ndx + 2) Then Exit Sub
            End If
            If (Pos4 >= 0) Then
                Servo.ID(Ndx + 3).Pos = Pos4
                If Servo.Max = (Ndx + 3) Then Exit Sub
            End If
            If (Pos5 >= 0) Then
                Servo.ID(Ndx + 4).Pos = Pos5
                If Servo.Max = (Ndx + 4) Then Exit Sub
            End If

            If (Pos6 >= 0) Then
                Servo.ID(Ndx + 5).Pos = Pos6
                If Servo.Max = (Ndx + 5) Then Exit Sub
            End If
            If (Pos7 >= 0) Then
                Servo.ID(Ndx + 6).Pos = Pos7
                If Servo.Max = (Ndx + 6) Then Exit Sub
            End If
            If (Pos8 >= 0) Then
                Servo.ID(Ndx + 7).Pos = Pos8
                If Servo.Max = (Ndx + 7) Then Exit Sub
            End If
            If (Pos9 >= 0) Then
                Servo.ID(Ndx + 8).Pos = Pos9
                If Servo.Max = (Ndx + 8) Then Exit Sub
            End If
            If (Pos10 >= 0) Then
                Servo.ID(Ndx + 9).Pos = Pos10
                If Servo.Max = (Ndx + 9) Then Exit Sub
            End If

        End Sub
    End Structure

    Public Servo As sServo


    '================================================================================================================================================
#Region "Serial Port"

    Public Sub Serial_Init(ByVal BaudRate As Long)
        Dim Ports As Array
        Dim i As Integer

        '### RS232
        Ports = IO.Ports.SerialPort.GetPortNames()
        If UBound(Ports) < 0 Then
            FMain.ToolStripStatusLabel1.Text = "SerialPort : Closed"
            FMain.ToolStripButton1.Image = Image.FromFile("port_OFF.png")
            'Me.Close()
        Else
            For i = 0 To UBound(Ports)
                FMain.ToolStripComboBox1.Items.Add(Ports(i))
            Next
            FMain.ToolStripComboBox1.Text = FMain.ToolStripComboBox1.Items.Item(0)
            FMain.ToolStripStatusLabel1.Text = "SerialPort : Closed"
            Serial_Open(FMain.ToolStripComboBox1.Text, BaudRate)
        End If
    End Sub

    Public Sub Serial_Open(ByVal Portame As String, ByVal BaudRate As Long)
        Try
            FMain.SerialPort1.PortName = Portame 'FMain.ToolStripComboBox1.Text
            FMain.SerialPort1.BaudRate = BaudRate
            FMain.SerialPort1.Open()

            'Update the StatusStrip
            FMain.ToolStripStatusLabel1.Text = "SerialPort : " + FMain.ToolStripComboBox1.Text + " Opened"
            FMain.ToolStripButton1.Image = Image.FromFile("port_ON.png")
        Catch ex As Exception
            'Unable to open the SerialPort - prompt the user
            MsgBox("Unable to Open SerialPort", MsgBoxStyle.Critical)
            FMain.ToolStripStatusLabel1.Text = "SerialPort : " + FMain.ToolStripComboBox1.Text + " Closed"
            FMain.ToolStripButton1.Image = Image.FromFile("port_OFF.png")
        End Try
    End Sub

#End Region
    '================================================================================================================================================

    '================================================================================================================================================
#Region "SCS15"


    Public Sub Servo_Pos()

    End Sub





    'Public Sub VM_TX(ByRef SerialPort1 As System.IO.Ports.SerialPort, ID As Integer, LENGTH As Integer, TXData() As Integer)
    '    If SerialPort1.IsOpen Then
    '        Dim B(20) As Byte
    '        Dim ChkSUm, ndx As Integer
    '        B(0) = &HFF : B(1) = &HFF       '<< Start 0xFF 0xFF
    '        B(2) = ID                       '<< ID
    '        B(3) = 2 + LENGTH                         '<< Length
    '        B(4) = INST_WRITE               '<< Instruction
    '        Dim COUNT As Integer = 5
    '        For I = 1 To LENGTH
    '            B(COUNT) = TXData(I + 2)
    '            COUNT = COUNT + 1
    '        Next

    '        ChkSUm = 0 '(B(2) + B(3) + B(4) + B(5) + B(6) + B(7) + B(8) + B(9) + B(10) + B(11)) Mod 256
    '        For ndx = 2 To (COUNT - 1)
    '            ChkSUm = ChkSUm + B(ndx)
    '        Next
    '        B(COUNT) = CByte((Not (ChkSUm)) And &HFF)
    '        SerialPort1.Write(B, 0, COUNT + 1)
    '    End If
    'End Sub

#End Region
    '================================================================================================================================================

    Public Function DelayMS(x As Integer) As Integer
        Dim sw As New Stopwatch
        sw.Reset()
        sw.Start()
        Dim ts As TimeSpan

        If x < 2 Then x = 2
        Do
            ts = sw.Elapsed()
            'If BackgroundWorker1.CancellationPending Then
            '    Return -1
            'End If
        Loop Until ts.TotalMilliseconds > x

        Return 0
    End Function


End Module
