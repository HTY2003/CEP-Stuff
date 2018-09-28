Module MBug

    Public Sub Position_Hip_Joint(ByVal Pos As Integer)
        Servo.ID(1).Pos = Servo.ID(1).InitPos + Pos
        Servo.ID(7).Pos = Servo.ID(7).InitPos + Pos
        Servo.ID(14).Pos = Servo.ID(14).InitPos + Pos

        Servo.ID(4).Pos = Servo.ID(4).InitPos - Pos
        Servo.ID(11).Pos = Servo.ID(11).InitPos - Pos
        Servo.ID(17).Pos = Servo.ID(17).InitPos - Pos
    End Sub

    Public Sub Position_Mid_Joint(ByVal Pos As Integer)
        Servo.ID(2).Pos = Servo.ID(2).InitPos + Pos
        Servo.ID(5).Pos = Servo.ID(5).InitPos + Pos
        Servo.ID(8).Pos = Servo.ID(8).InitPos + Pos

        Servo.ID(12).Pos = Servo.ID(12).InitPos - Pos
        Servo.ID(15).Pos = Servo.ID(15).InitPos - Pos
        Servo.ID(18).Pos = Servo.ID(18).InitPos - Pos
    End Sub
    Public Sub Position_End_Leg(ByVal Pos As Integer)
        Servo.ID(3).Pos = Servo.ID(3).InitPos + Pos
        Servo.ID(6).Pos = Servo.ID(6).InitPos + Pos
        Servo.ID(9).Pos = Servo.ID(9).InitPos + Pos

        Servo.ID(13).Pos = Servo.ID(13).InitPos - Pos
        Servo.ID(16).Pos = Servo.ID(16).InitPos - Pos
        Servo.ID(19).Pos = Servo.ID(19).InitPos - Pos
    End Sub



    Public Sub Position_Alt_RightL(ByVal Pos As Integer)
        Servo.ID(2).Pos = Servo.ID(2).InitPos + Pos
        'Servo.ID(5).Pos = Servo.ID(5).InitPos + Pos
        Servo.ID(8).Pos = Servo.ID(8).InitPos + Pos

        'Servo.ID(12).Pos = Servo.ID(12).InitPos - Pos
        Servo.ID(15).Pos = Servo.ID(15).InitPos - Pos
        'Servo.ID(18).Pos = Servo.ID(18).InitPos - Pos
    End Sub
    Public Sub Position_Alt_LeftL(ByVal Pos As Integer)
        'Servo.ID(2).Pos = Servo.ID(2).InitPos + Pos
        Servo.ID(5).Pos = Servo.ID(5).InitPos + Pos
        'Servo.ID(8).Pos = Servo.ID(8).InitPos + Pos

        Servo.ID(12).Pos = Servo.ID(12).InitPos - Pos
        'Servo.ID(15).Pos = Servo.ID(15).InitPos - Pos
        Servo.ID(18).Pos = Servo.ID(18).InitPos - Pos
    End Sub

    Public Sub Position_Alt_SwingHip(ByVal Pos As Integer)
        Servo.ID(1).Pos = Servo.ID(1).InitPos - Pos
        Servo.ID(7).Pos = Servo.ID(7).InitPos - Pos
        Servo.ID(14).Pos = Servo.ID(14).InitPos - Pos
        '--------
        Servo.ID(4).Pos = Servo.ID(4).InitPos + Pos
        Servo.ID(11).Pos = Servo.ID(11).InitPos + Pos
        Servo.ID(17).Pos = Servo.ID(17).InitPos + Pos
    End Sub




End Module
