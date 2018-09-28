Public Class FMain
    '#Const Bot = 1
#Const Bot = 2

    '================================================================================================================================================
    Private BaudRate As Long = 1000000
    'Private BaudRate As Long = 115200

#Region "Menu"
    Private Sub RunToolStripMenuItem_Click(sender As System.Object, e As System.EventArgs) Handles RunToolStripMenuItem.Click
        ToolStripButton2.PerformClick()
    End Sub
    Private Sub StopToolStripMenuItem_Click(sender As System.Object, e As System.EventArgs) Handles StopToolStripMenuItem.Click
        ToolStripButton3.PerformClick()
    End Sub

    Private Sub ScanToolStripMenuItem_Click(sender As System.Object, e As System.EventArgs) Handles ScanToolStripMenuItem.Click
        ToolStripButton4.PerformClick()
    End Sub

    Private Sub ScanClearToolStripMenuItem_Click(sender As System.Object, e As System.EventArgs) Handles ScanClearToolStripMenuItem.Click
        DebugW.Text = ""
        ToolStripButton4.PerformClick()
    End Sub
#End Region

#Region "ToolStrip"
    Private Sub ToolStripButton1_Click(sender As System.Object, e As System.EventArgs) Handles ToolStripButton1.Click
        'Serial Open/Close
        If SerialPort1.IsOpen Then
            SerialPort1.Close()
            ToolStripButton1.Image = Image.FromFile("port_OFF.png")
        Else
            Serial_Open(ToolStripComboBox1.Text, BaudRate)
        End If
    End Sub

    Private Sub ToolStripButton2_Click(sender As System.Object, e As System.EventArgs) Handles ToolStripButton2.Click
        'Run
        Try
            BackgroundWorker1.WorkerSupportsCancellation = True
            BackgroundWorker1.RunWorkerAsync()
        Catch ex As Exception
            MsgBox("Background Run ERR")
        End Try
    End Sub
    Private Sub ToolStripButton3_Click(sender As System.Object, e As System.EventArgs) Handles ToolStripButton3.Click
        'Stop
        While BackgroundWorker1.IsBusy
            Application.DoEvents()
        End While
        MsgBox("Stop")
    End Sub

    Private Sub ToolStripButton4_Click(sender As System.Object, e As System.EventArgs) Handles ToolStripButton4.Click
        'Read all servos
        Dim i As Integer
        DebugW.Text = DebugW.Text + "Servo Physical Position" + vbCrLf
        For i = 1 To Servo.Max
            Dim pos As Integer = SCS15_Get_Position(SerialPort1, i)
            DebugW.Text = DebugW.Text + "ID : " + CStr(i) + "  -  " + CStr(pos) + vbCrLf
        Next
    End Sub

    Private Sub ToolStripButton5_Click(sender As System.Object, e As System.EventArgs) Handles ToolStripButton5.Click
        'Dim i As Integer
        'DebugW.Text = DebugW.Text + "Servo Init/Position" + vbCrLf
        'For i = 1 To Servo.Max
        '    DebugW.Text = DebugW.Text + "ID : " + CStr(Servo.ID(i).InitPos) + "  ,  " + CStr(Servo.ID(i).Pos) + vbCrLf
        'Next


    End Sub
#End Region

#Region "Controls"
    Private Sub DebugW_DoubleClick(sender As Object, e As System.EventArgs) Handles DebugW.DoubleClick
        DebugW.Text = ""
    End Sub

    Public GRxMode As Integer = 1
    Private Sub SerialPort1_DataReceived(sender As System.Object, e As System.IO.Ports.SerialDataReceivedEventArgs) Handles SerialPort1.DataReceived
        'Reading from the SerialPort
        If GRxMode = 1 Then
            Dim B(100) As Byte
            Dim D, I As Integer
            Dim Str As String = ""

            D = SerialPort1.Read(B, 0, 100)
            For I = 0 To D - 1
                If B(I) = 13 Then
                    Str = Str + vbCrLf
                Else
                    Str = Str + B(I).ToString + " " 'Chr(B(I))
                    'Str = Str + Hex(I).ToString  ' Chr(B(I))
                End If
            Next
            'SetText2(Str)
        End If
    End Sub

    Private Sub FMain_FormClosing(sender As Object, e As System.Windows.Forms.FormClosingEventArgs) Handles Me.FormClosing
        Bug.Cmd = eCmd.eQuit
        DelayMS(1000)

        If BackgroundWorker1.IsBusy Then
            BackgroundWorker1.CancelAsync()
            While BackgroundWorker1.IsBusy
                Application.DoEvents()
            End While
        End If

    End Sub

    Delegate Sub SetTextCallback_TextBox3(ByVal [text] As String)
    Private Sub SetText_TextBox3(ByVal [text] As String)
        If Me.TextBox3.InvokeRequired Then
            Dim d As New SetTextCallback_TextBox3(AddressOf SetText_TextBox3)
            Me.Invoke(d, New Object() {[text]})
        Else
            Me.TextBox3.Text = [text]
        End If
    End Sub

    Delegate Sub SetTextCallback_DebugW(ByVal [text] As String)
    Private Sub SetText_DebugW(ByVal [text] As String)
        If Me.DebugW.InvokeRequired Then
            Dim d As New SetTextCallback_DebugW(AddressOf SetText_DebugW)
            Me.Invoke(d, New Object() {[text]})
        Else
            Me.DebugW.Text = Me.DebugW.Text + [text]
        End If
    End Sub
    Public Sub DebugW_Print(ByVal Str As String)
        SetText_DebugW(Str + vbCrLf)
    End Sub


#End Region


    Public Enum eCmd
        eIdle

        eInitPos

        eStand
        eSit


        eStop
        eWalk_Stationary
        eWalk_Forward
        eWalk_Reverse
        eWalk_Side_Left
        eWalk_Side_Right

        eWalk_Pivot_Left
        eWalk_Pivot_Right
        eQuit

    End Enum

    Public Structure sBug
        Public Cmd As eCmd
        Public Stand_Ht As Integer

        Public Speed As Integer
        Public Swing As Integer
        Public TurningSpeed As Integer

        Public Sub Init()
            Stand_Ht = -250

            Speed = 300
            Swing = 40
            TurningSpeed = 50

        End Sub


        Public Sub P_Init(ByVal T As Integer)
            'Servo.ID(1).Pos = Servo.ID(1).InitPos '- Pos
            'Servo.ID(7).Pos = Servo.ID(7).InitPos '- Pos
            'Servo.ID(14).Pos = Servo.ID(14).InitPos '- Pos

            'Servo.ID(4).Pos = Servo.ID(4).InitPos '+ Pos
            'Servo.ID(11).Pos = Servo.ID(11).InitPos '+ Pos
            'Servo.ID(17).Pos = Servo.ID(17).InitPos '+ Pos
            Dim i As Integer
            For i = 1 To 19
                Servo.ID(i).Pos = Servo.ID(i).InitPos
            Next

            Servo.SetAllPos(T)
        End Sub

        Public Sub P_Stand(ByVal T As Integer)
            Position_Mid_Joint(Stand_Ht)
            Servo.SetAllPos(T)
        End Sub
        Public Sub P_Sit(ByVal T As Integer)
            Position_Mid_Joint(90) '-Stand_Ht)
            Servo.SetAllPos(T)
        End Sub

        Public Sub Walk_Stop(ByVal T As Integer)
            Servo.ID(1).Pos = Servo.ID(1).InitPos '- Pos
            Servo.ID(7).Pos = Servo.ID(7).InitPos '- Pos
            Servo.ID(14).Pos = Servo.ID(14).InitPos '- Pos

            Servo.ID(4).Pos = Servo.ID(4).InitPos '+ Pos
            Servo.ID(11).Pos = Servo.ID(11).InitPos '+ Pos
            Servo.ID(17).Pos = Servo.ID(17).InitPos '+ Pos

            Position_End_Leg(0)
            Position_Mid_Joint(Stand_Ht)

            'Servo.Init_AllPosition()
            'Servo.Position_L2(Stand_Ht)
            'P_Stand(T)
            Servo.SetAllPos(T)
        End Sub
        Public Sub Walk_Stationary(ByVal T As Integer)
            Position_Alt_RightL(-150)
            Servo.SetAllPos(T)
            Position_Alt_RightL(-250)
            Servo.SetAllPos(T)

            Position_Alt_LeftL(-150)
            Servo.SetAllPos(T)
            Position_Alt_LeftL(-250)
            Servo.SetAllPos(T)
        End Sub
        Public Sub Walk_Straight(ByVal T As Integer, ByVal Swing As Integer)
            'PART 1
            Position_Alt_RightL(-150) 'UP
            Position_Alt_SwingHip(0)
            Servo.SetAllPos(T)
            Position_Alt_RightL(-250) 'Ground
            Position_Alt_SwingHip(Swing)
            Servo.SetAllPos(T)

            'PART 2
            Position_Alt_LeftL(-150) 'UP
            Position_Alt_SwingHip(0)
            Servo.SetAllPos(T)
            Position_Alt_LeftL(-250) 'Ground
            Position_Alt_SwingHip(-Swing)
            Servo.SetAllPos(T)
        End Sub

        Public Sub Walk_Side(ByVal T As Integer, ByVal Swing As Integer)
            'PART 1
            Position_Alt_RightL(-150) 'UP 2,8,15
            Servo.ID(3).Pos = Servo.ID(3).InitPos - Swing
            Servo.ID(9).Pos = Servo.ID(9).InitPos - Swing
            Servo.ID(16).Pos = Servo.ID(16).InitPos - Swing

            Servo.ID(6).Pos = Servo.ID(6).InitPos
            Servo.ID(13).Pos = Servo.ID(13).InitPos
            Servo.ID(19).Pos = Servo.ID(19).InitPos
            Servo.SetAllPos(T)

            Position_Alt_RightL(-250) 'Ground
            'Position_Alt_SwingHip(Swing)
            Servo.SetAllPos(T)

            ''PART 2
            Position_Alt_LeftL(-150) 'UP
            Servo.ID(3).Pos = Servo.ID(3).InitPos
            Servo.ID(9).Pos = Servo.ID(9).InitPos
            Servo.ID(16).Pos = Servo.ID(16).InitPos

            Servo.ID(6).Pos = Servo.ID(6).InitPos - Swing
            Servo.ID(13).Pos = Servo.ID(13).InitPos - Swing
            Servo.ID(19).Pos = Servo.ID(19).InitPos - Swing
            Servo.SetAllPos(T)

            Position_Alt_LeftL(-250) 'Ground
            'Position_Alt_SwingHip(-Swing)
            Servo.SetAllPos(T)
        End Sub

        Public Sub Walk_Pivot(ByVal T As Integer, ByVal Swing As Integer)
            'PART 1
            Position_Alt_RightL(-150) 'UP 2,8,15
            Servo.ID(1).Pos = Servo.ID(1).InitPos '+ Swing
            Servo.ID(7).Pos = Servo.ID(7).InitPos '+ Swing
            Servo.ID(14).Pos = Servo.ID(14).InitPos '- Swing

            Servo.ID(4).Pos = Servo.ID(4).InitPos '- Swing
            Servo.ID(11).Pos = Servo.ID(11).InitPos '+ Swing
            Servo.ID(17).Pos = Servo.ID(17).InitPos '+ Swing
            Servo.SetAllPos(T)

            Position_Alt_RightL(-250) 'Ground
            Servo.ID(1).Pos = Servo.ID(1).InitPos + Swing
            Servo.ID(7).Pos = Servo.ID(7).InitPos + Swing
            Servo.ID(14).Pos = Servo.ID(14).InitPos - Swing

            Servo.ID(4).Pos = Servo.ID(4).InitPos - Swing
            Servo.ID(11).Pos = Servo.ID(11).InitPos + Swing
            Servo.ID(17).Pos = Servo.ID(17).InitPos + Swing
            Servo.SetAllPos(T)

            'PART 2
            Position_Alt_LeftL(-150) 'UP
            Servo.ID(1).Pos = Servo.ID(1).InitPos '+ Swing
            Servo.ID(7).Pos = Servo.ID(7).InitPos '+ Swing
            Servo.ID(14).Pos = Servo.ID(14).InitPos '- Swing

            Servo.ID(4).Pos = Servo.ID(4).InitPos '- Swing
            Servo.ID(11).Pos = Servo.ID(11).InitPos '+ Swing
            Servo.ID(17).Pos = Servo.ID(17).InitPos '+ Swing
            Servo.SetAllPos(T)

            Position_Alt_LeftL(-250) 'Ground
            Servo.ID(1).Pos = Servo.ID(1).InitPos - Swing
            Servo.ID(7).Pos = Servo.ID(7).InitPos - Swing
            Servo.ID(14).Pos = Servo.ID(14).InitPos + Swing

            Servo.ID(4).Pos = Servo.ID(4).InitPos + Swing
            Servo.ID(11).Pos = Servo.ID(11).InitPos - Swing
            Servo.ID(17).Pos = Servo.ID(17).InitPos - Swing
            Servo.SetAllPos(T)
        End Sub



    End Structure
    Public Bug As sBug


#Region "Test"
    'Test Buttons
    Private Sub Button1_Click(sender As System.Object, e As System.EventArgs) Handles Button1.Click
        'Servo.Position(100, , 300)

        Bug.P_Stand(1800)


    End Sub

    Private Sub Button2_Click(sender As System.Object, e As System.EventArgs) Handles Button2.Click
        'Servo.Position_Ndx(2, 222, 333, 444, 555, 666, 777)

        Bug.P_Sit(1500)

    End Sub



    Private Sub TextBox1_DoubleClick(sender As Object, e As System.EventArgs) Handles TextBox1.DoubleClick
        Dim Pos As Integer
        Try
            Pos = CInt(TextBox1.Text)
            SCS15_Set_Position(SerialPort1, 1, Pos, 500)
        Catch ex As Exception
            MsgBox("Button1 Err")
        End Try
    End Sub

    Private Sub TextBox2_DoubleClick(sender As Object, e As System.EventArgs) Handles TextBox2.DoubleClick
        Dim Pos As Integer
        Try
            Pos = CInt(TextBox2.Text)
            SCS15_Set_Position(SerialPort1, 1, Pos, 500)
        Catch ex As Exception
            MsgBox("Button1 Err")
        End Try
    End Sub

#End Region

    '================================================================================================================================================
    'Start
    Private Sub FMain_Load(sender As System.Object, e As System.EventArgs) Handles MyBase.Load
        Serial_Init(BaudRate)
        'Serial_Open("COM20", BaudRate)
        DebugW.Text = ""

        Servo.Init(25)

#If Bot = 1 Then



        Servo.ID(1).InitPos = 498
        Servo.ID(2).InitPos = 410 + 70
        Servo.ID(3).InitPos = 530 - 100

        Servo.ID(4).InitPos = 510 '517
        Servo.ID(5).InitPos = 490 + 70
        Servo.ID(6).InitPos = 510 - 100

        Servo.ID(7).InitPos = 519
        Servo.ID(8).InitPos = 535 + 70
        Servo.ID(9).InitPos = 520 - 100

        Servo.ID(10).InitPos = 511

        Servo.ID(11).InitPos = 505
        Servo.ID(12).InitPos = 530 - 70
        Servo.ID(13).InitPos = 455 + 100

        Servo.ID(14).InitPos = 485
        Servo.ID(15).InitPos = 500 - 70
        Servo.ID(16).InitPos = 520 + 100

        Servo.ID(17).InitPos = 530
        Servo.ID(18).InitPos = 510 - 70
        Servo.ID(19).InitPos = 510 + 100

        Servo.ID(20).InitPos = 511

#ElseIf Bot = 2 Then
        Servo.ID(1).InitPos = 498
        Servo.ID(2).InitPos = 410 + 70
        Servo.ID(3).InitPos = 530 - 100

        Servo.ID(4).InitPos = 510 '517
        Servo.ID(5).InitPos = 490 + 70
        Servo.ID(6).InitPos = 510 - 100

        Servo.ID(7).InitPos = 519
        Servo.ID(8).InitPos = 535 + 70
        Servo.ID(9).InitPos = 520 - 100

        Servo.ID(10).InitPos = 511

        Servo.ID(11).InitPos = 505
        Servo.ID(12).InitPos = 530 - 70
        Servo.ID(13).InitPos = 455 + 100

        Servo.ID(14).InitPos = 485
        Servo.ID(15).InitPos = 500 - 70
        Servo.ID(16).InitPos = 520 + 100

        Servo.ID(17).InitPos = 530
        Servo.ID(18).InitPos = 510 - 70
        Servo.ID(19).InitPos = 510 + 100

        Servo.ID(20).InitPos = 511
        Servo.ID(21).InitPos = 511
        Servo.ID(22).InitPos = 511
        Servo.ID(23).InitPos = 511
        Servo.ID(24).InitPos = 511
        Servo.ID(25).InitPos = 511
#Else
        MsgBox("Err")

        Me.Close()
        Exit Sub
#End If

        Servo.Init_AllPosition()

        Bug.Init()
        'Servo.SerialPort1 = Me.SerialPort1

        'Dim i As Integer
        'For i = 1 To 19
        '    Servo.ID(i).Pos = Servo.ID(i).InitPos
        'Next

        'Servo.SetAllPos(800)

        'Servo.ID(i).Pos = Servo.ID(i).InitPos + 100
        'Servo.SetAllPos(800)




        'Do

        'Loop



        Try
            BackgroundWorker1.WorkerSupportsCancellation = True
            BackgroundWorker1.RunWorkerAsync()
        Catch ex As Exception
            MsgBox("Background Run ERR")
        End Try


        'For i = 1 To 19
        '    Servo.ID(i).Pos = Servo.ID(i).InitPos
        'Next
        'Servo.SetAllPos(800)


        'DelayMS(1500)
        'Me.Close()

    End Sub

    '================================================================================================================================================
    'Main Loop
    Private Sub BackgroundWorker1_DoWork(sender As System.Object, e As System.ComponentModel.DoWorkEventArgs) Handles BackgroundWorker1.DoWork
        'Run
        Servo.SerialPort1 = Me.SerialPort1
        If Not Servo.SerialPort1.IsOpen Then
            Exit Sub
        End If
        DebugW_Print("Start")

        'Bug.P_Stand(800)

        Do
            Select Case Bug.Cmd
                Case eCmd.eStand
                    Bug.Walk_Stop(300)
                    Bug.P_Stand(1800)
                    Bug.Cmd = eCmd.eIdle

                Case eCmd.eSit
                    Bug.Walk_Stop(300)
                    Bug.P_Sit(1000)
                    Bug.Cmd = eCmd.eIdle

                Case eCmd.eWalk_Stationary
                    Bug.Walk_Stationary(Bug.Speed)

                Case eCmd.eStop
                    Bug.Walk_Stop(300)
                    Bug.Cmd = eCmd.eIdle

                Case eCmd.eWalk_Forward
                    Bug.Walk_Straight(Bug.Speed, Bug.Swing)
                Case eCmd.eWalk_Reverse
                    Bug.Walk_Straight(Bug.Speed, -Bug.Swing)

                Case eCmd.eWalk_Side_Right
                    Bug.Walk_Side(Bug.Speed, Bug.Swing)
                Case eCmd.eWalk_Side_Left
                    Bug.Walk_Side(Bug.Speed, -Bug.Swing)

                Case eCmd.eWalk_Pivot_Left
                    Bug.Walk_Pivot(Bug.Speed, Bug.TurningSpeed)
                Case eCmd.eWalk_Pivot_Right
                    Bug.Walk_Pivot(Bug.Speed, -Bug.TurningSpeed)

                Case eCmd.eInitPos
                    Bug.P_Init(800)

                Case eCmd.eQuit

                    Exit Do
                Case Else
                    'do nothing

            End Select
        Loop

        'DelayMS(1000)
        'Servo.SetAllPos2Init(800)
        DebugW_Print("Done")
    End Sub


    Private Sub Button3_Click(sender As System.Object, e As System.EventArgs) Handles Button3.Click
        Bug.Cmd = eCmd.eWalk_Stationary
    End Sub
    Private Sub Button4_Click(sender As System.Object, e As System.EventArgs) Handles Button4.Click
        Bug.Cmd = eCmd.eStop
    End Sub
    Private Sub Button5_Click(sender As System.Object, e As System.EventArgs) Handles Button5.Click
        Bug.Cmd = eCmd.eWalk_Forward
    End Sub
    Private Sub Button6_Click(sender As System.Object, e As System.EventArgs) Handles Button6.Click
        Bug.Cmd = eCmd.eWalk_Reverse
    End Sub
    Private Sub Button7_Click(sender As System.Object, e As System.EventArgs) Handles Button7.Click
        Bug.Cmd = eCmd.eWalk_Side_Left
    End Sub
    Private Sub Button8_Click(sender As System.Object, e As System.EventArgs) Handles Button8.Click
        Bug.Cmd = eCmd.eWalk_Side_Right
    End Sub
    Private Sub Button9_Click(sender As System.Object, e As System.EventArgs) Handles Button9.Click
        Bug.Cmd = eCmd.eWalk_Pivot_Left
    End Sub
    Private Sub Button10_Click(sender As System.Object, e As System.EventArgs) Handles Button10.Click
        Bug.Cmd = eCmd.eWalk_Pivot_Right
    End Sub
    Private Sub Button11_Click(sender As System.Object, e As System.EventArgs)
        'Bug.P_Init(800)
        Bug.Cmd = eCmd.eInitPos
    End Sub


    Private Sub StopToolStripMenuItem1_Click(sender As System.Object, e As System.EventArgs) Handles StopToolStripMenuItem1.Click
        Bug.Cmd = eCmd.eStop
    End Sub
    Private Sub WForwardToolStripMenuItem_Click(sender As System.Object, e As System.EventArgs) Handles WForwardToolStripMenuItem.Click
        Bug.Cmd = eCmd.eWalk_Forward
    End Sub
    Private Sub WReverseToolStripMenuItem_Click(sender As System.Object, e As System.EventArgs) Handles WReverseToolStripMenuItem.Click
        Bug.Cmd = eCmd.eWalk_Reverse
    End Sub
    Private Sub WStationaryToolStripMenuItem_Click(sender As System.Object, e As System.EventArgs) Handles WStationaryToolStripMenuItem.Click
        Bug.Cmd = eCmd.eWalk_Stationary
    End Sub
    Private Sub WSideLeftToolStripMenuItem_Click(sender As System.Object, e As System.EventArgs) Handles WSideLeftToolStripMenuItem.Click
        Bug.Cmd = eCmd.eWalk_Side_Left
    End Sub
    Private Sub WSideRightToolStripMenuItem_Click(sender As System.Object, e As System.EventArgs) Handles WSideRightToolStripMenuItem.Click
        Bug.Cmd = eCmd.eWalk_Side_Right
    End Sub
    Private Sub WPivotLeftToolStripMenuItem_Click(sender As System.Object, e As System.EventArgs) Handles WPivotLeftToolStripMenuItem.Click
        Bug.Cmd = eCmd.eWalk_Pivot_Left
    End Sub
    Private Sub WPivotRightToolStripMenuItem_Click(sender As System.Object, e As System.EventArgs) Handles WPivotRightToolStripMenuItem.Click
        Bug.Cmd = eCmd.eWalk_Pivot_Right
    End Sub
    Private Sub StandToolStripMenuItem_Click(sender As System.Object, e As System.EventArgs) Handles StandToolStripMenuItem.Click
        Bug.Cmd = eCmd.eStand
    End Sub
    Private Sub SitToolStripMenuItem_Click(sender As System.Object, e As System.EventArgs) Handles SitToolStripMenuItem.Click
        Bug.Cmd = eCmd.eSit
    End Sub

    Private Sub TextBox3_KeyUp(sender As Object, e As System.Windows.Forms.KeyEventArgs) Handles TextBox3.KeyUp
        If e.KeyCode = Keys.Enter Then
            Try
                Bug.Speed = CInt(TextBox3.Text)
            Catch ex As Exception
                Bug.Speed = 300 'default
            End Try
        End If
    End Sub

    Private Sub TextBox4_KeyUp(sender As Object, e As System.Windows.Forms.KeyEventArgs) Handles TextBox4.KeyUp
        If e.KeyCode = Keys.Enter Then
            Try
                Bug.Swing = CInt(TextBox4.Text)
            Catch ex As Exception
                Bug.Swing = 40 'default
            End Try
        End If
    End Sub
    Private Sub TextBox5_KeyUp(sender As Object, e As System.Windows.Forms.KeyEventArgs) Handles TextBox5.KeyUp
        If e.KeyCode = Keys.Enter Then
            Try
                Bug.TurningSpeed = CInt(TextBox4.Text)
            Catch ex As Exception
                Bug.TurningSpeed = 50 'default
            End Try
        End If
    End Sub

    Private Sub Button12_Click(sender As Object, e As EventArgs) Handles Button12.Click
        Dim x As Integer = 0
        While x < 5
            Bug.Cmd = eCmd.eWalk_Pivot_Left
            DelayMS(900)
            Bug.Cmd = eCmd.eWalk_Pivot_Right
            DelayMS(900)
            x += 1
        End While
        Bug.Cmd = eCmd.eStop
    End Sub

    Private Sub ForwardToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles ForwardToolStripMenuItem.Click
        Bug.Cmd = eCmd.eWalk_Reverse
    End Sub

    Private Sub BackwardToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles BackwardToolStripMenuItem.Click
        Bug.Cmd = eCmd.eWalk_Forward
    End Sub

    Private Sub TurnLeftToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles TurnLeftToolStripMenuItem.Click
        Bug.Cmd = eCmd.eWalk_Pivot_Left
    End Sub

    Private Sub TurnRightToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles TurnRightToolStripMenuItem.Click
        Bug.Cmd = eCmd.eWalk_Pivot_Right
    End Sub

    Private Sub MarchLeftToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles MarchLeftToolStripMenuItem.Click
        Bug.Cmd = eCmd.eWalk_Side_Right
    End Sub

    Private Sub MarchRightToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles MarchRightToolStripMenuItem.Click
        Bug.Cmd = eCmd.eWalk_Side_Right
    End Sub

    Private Sub StopToolStripMenuItem2_Click(sender As Object, e As EventArgs) Handles StopToolStripMenuItem2.Click
        Bug.Cmd = eCmd.eStop
    End Sub

    Private Sub MarchOnTheSpotToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles MarchOnTheSpotToolStripMenuItem.Click
        Bug.Cmd = eCmd.eWalk_Stationary
    End Sub

    Private Sub VictoryDanceToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles VictoryDanceToolStripMenuItem.Click
        Dim x As Integer = 0
        While x < 5
            Bug.Cmd = eCmd.eWalk_Pivot_Left
            DelayMS(900)
            Bug.Cmd = eCmd.eWalk_Pivot_Right
            DelayMS(900)
            x += 1
        End While
        Servo.ID(20).Pos = 511
        Servo.ID(21).Pos = 511
        Servo.ID(22).Pos = 511
        Servo.ID(23).Pos = 511
        Servo.ID(24).Pos = 511
        Servo.ID(25).Pos = 511
        Bug.Cmd = eCmd.eStop

    End Sub

    Private Sub Button13_Click(sender As Object, e As EventArgs) Handles Button13.Click

        Servo.ID(20).Pos = 511
        Servo.ID(21).Pos = 511 + 410
        Servo.ID(22).Pos = 511 - 100
        Servo.ID(23).Pos = 511 - 180
        Servo.ID(24).Pos = 511 - 180
        Servo.ID(25).Pos = 511 - 150

        Servo.SetAllPos(200)

        Servo.ID(20).Pos = 511 + 400
        Servo.ID(21).Pos = 511
        Servo.ID(22).Pos = 511
        Servo.ID(23).Pos = 511
        Servo.ID(24).Pos = 511
        Servo.ID(25).Pos = 511

        Servo.SetAllPos(100)

    End Sub

    Private Sub StabToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles StabToolStripMenuItem.Click
        Servo.ID(20).Pos = 511 - 200
        Servo.ID(21).Pos = 511 + 410
        Servo.ID(22).Pos = 511 - 100
        Servo.ID(23).Pos = 511 - 180
        Servo.ID(24).Pos = 511 - 180
        Servo.ID(25).Pos = 511 - 150

        Servo.SetAllPos(200)

        Servo.ID(20).Pos = 511 + 350
        Servo.ID(21).Pos = 511
        Servo.ID(22).Pos = 511
        Servo.ID(23).Pos = 511
        Servo.ID(24).Pos = 511
        Servo.ID(25).Pos = 511

        Servo.SetAllPos(100)

    End Sub

    Private Sub Button11_Click_1(sender As Object, e As EventArgs)
        Bug.P_Stand(1800)
        DelayMS(1000)
        Bug.Cmd = eCmd.eWalk_Stationary




    End Sub

    Private Sub MenuStrip1_ItemClicked(sender As Object, e As ToolStripItemClickedEventArgs) Handles MenuStrip1.ItemClicked

    End Sub
End Class
