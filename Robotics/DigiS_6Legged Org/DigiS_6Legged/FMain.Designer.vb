<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
Partial Class FMain
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()>
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()>
    Private Sub InitializeComponent()
        Me.components = New System.ComponentModel.Container()
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(FMain))
        Me.SerialPort1 = New System.IO.Ports.SerialPort(Me.components)
        Me.StatusStrip1 = New System.Windows.Forms.StatusStrip()
        Me.ToolStripStatusLabel1 = New System.Windows.Forms.ToolStripStatusLabel()
        Me.MenuStrip1 = New System.Windows.Forms.MenuStrip()
        Me.FileToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.CloseToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.BugToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.StopToolStripMenuItem1 = New System.Windows.Forms.ToolStripMenuItem()
        Me.WForwardToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.WReverseToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.WStationaryToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.WSideLeftToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.WSideRightToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.WPivotLeftToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.WPivotRightToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.StandToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.SitToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.CommandToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.RunToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.StopToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.ToolStripMenuItem1 = New System.Windows.Forms.ToolStripSeparator()
        Me.ScanToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.ScanClearToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.ToolStripMenuItem2 = New System.Windows.Forms.ToolStripSeparator()
        Me.ForwardToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.BackwardToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.TurnLeftToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.TurnRightToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.MarchLeftToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.MarchRightToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.StopToolStripMenuItem2 = New System.Windows.Forms.ToolStripMenuItem()
        Me.MarchOnTheSpotToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.VictoryDanceToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.StabToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.ToolStrip1 = New System.Windows.Forms.ToolStrip()
        Me.ToolStripButton1 = New System.Windows.Forms.ToolStripButton()
        Me.ToolStripComboBox1 = New System.Windows.Forms.ToolStripComboBox()
        Me.ToolStripSeparator1 = New System.Windows.Forms.ToolStripSeparator()
        Me.ToolStripButton3 = New System.Windows.Forms.ToolStripButton()
        Me.ToolStripButton2 = New System.Windows.Forms.ToolStripButton()
        Me.ToolStripButton4 = New System.Windows.Forms.ToolStripButton()
        Me.ToolStripButton5 = New System.Windows.Forms.ToolStripButton()
        Me.ToolStripSeparator2 = New System.Windows.Forms.ToolStripSeparator()
        Me.ToolStripTextBox1 = New System.Windows.Forms.ToolStripTextBox()
        Me.BackgroundWorker1 = New System.ComponentModel.BackgroundWorker()
        Me.ImageList1 = New System.Windows.Forms.ImageList(Me.components)
        Me.Button1 = New System.Windows.Forms.Button()
        Me.Button2 = New System.Windows.Forms.Button()
        Me.DebugW = New System.Windows.Forms.TextBox()
        Me.TextBox3 = New System.Windows.Forms.TextBox()
        Me.Button3 = New System.Windows.Forms.Button()
        Me.Button4 = New System.Windows.Forms.Button()
        Me.Button5 = New System.Windows.Forms.Button()
        Me.Button6 = New System.Windows.Forms.Button()
        Me.Button7 = New System.Windows.Forms.Button()
        Me.Button8 = New System.Windows.Forms.Button()
        Me.Button9 = New System.Windows.Forms.Button()
        Me.Button10 = New System.Windows.Forms.Button()
        Me.TextBox4 = New System.Windows.Forms.TextBox()
        Me.TextBox5 = New System.Windows.Forms.TextBox()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.Label3 = New System.Windows.Forms.Label()
        Me.Button12 = New System.Windows.Forms.Button()
        Me.TextBox2 = New System.Windows.Forms.TextBox()
        Me.TextBox1 = New System.Windows.Forms.TextBox()
        Me.Button13 = New System.Windows.Forms.Button()
        Me.StatusStrip1.SuspendLayout()
        Me.MenuStrip1.SuspendLayout()
        Me.ToolStrip1.SuspendLayout()
        Me.SuspendLayout()
        '
        'SerialPort1
        '
        Me.SerialPort1.BaudRate = 1000000
        Me.SerialPort1.PortName = "COM4"
        '
        'StatusStrip1
        '
        Me.StatusStrip1.ImageScalingSize = New System.Drawing.Size(32, 32)
        Me.StatusStrip1.Items.AddRange(New System.Windows.Forms.ToolStripItem() {Me.ToolStripStatusLabel1})
        Me.StatusStrip1.Location = New System.Drawing.Point(0, 1022)
        Me.StatusStrip1.Name = "StatusStrip1"
        Me.StatusStrip1.Padding = New System.Windows.Forms.Padding(2, 0, 33, 0)
        Me.StatusStrip1.Size = New System.Drawing.Size(1754, 42)
        Me.StatusStrip1.TabIndex = 0
        Me.StatusStrip1.Text = "StatusStrip1"
        '
        'ToolStripStatusLabel1
        '
        Me.ToolStripStatusLabel1.Name = "ToolStripStatusLabel1"
        Me.ToolStripStatusLabel1.Size = New System.Drawing.Size(271, 37)
        Me.ToolStripStatusLabel1.Text = "ToolStripStatusLabel1"
        '
        'MenuStrip1
        '
        Me.MenuStrip1.ImageScalingSize = New System.Drawing.Size(32, 32)
        Me.MenuStrip1.Items.AddRange(New System.Windows.Forms.ToolStripItem() {Me.FileToolStripMenuItem, Me.BugToolStripMenuItem, Me.CommandToolStripMenuItem})
        Me.MenuStrip1.Location = New System.Drawing.Point(0, 0)
        Me.MenuStrip1.Name = "MenuStrip1"
        Me.MenuStrip1.Padding = New System.Windows.Forms.Padding(14, 5, 0, 5)
        Me.MenuStrip1.Size = New System.Drawing.Size(1754, 51)
        Me.MenuStrip1.TabIndex = 1
        Me.MenuStrip1.Text = "MenuStrip1"
        '
        'FileToolStripMenuItem
        '
        Me.FileToolStripMenuItem.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.CloseToolStripMenuItem})
        Me.FileToolStripMenuItem.Name = "FileToolStripMenuItem"
        Me.FileToolStripMenuItem.Size = New System.Drawing.Size(70, 43)
        Me.FileToolStripMenuItem.Text = "File"
        '
        'CloseToolStripMenuItem
        '
        Me.CloseToolStripMenuItem.Name = "CloseToolStripMenuItem"
        Me.CloseToolStripMenuItem.Size = New System.Drawing.Size(189, 42)
        Me.CloseToolStripMenuItem.Text = "Close"
        '
        'BugToolStripMenuItem
        '
        Me.BugToolStripMenuItem.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.StopToolStripMenuItem1, Me.WForwardToolStripMenuItem, Me.WReverseToolStripMenuItem, Me.WStationaryToolStripMenuItem, Me.WSideLeftToolStripMenuItem, Me.WSideRightToolStripMenuItem, Me.WPivotLeftToolStripMenuItem, Me.WPivotRightToolStripMenuItem, Me.StandToolStripMenuItem, Me.SitToolStripMenuItem})
        Me.BugToolStripMenuItem.Name = "BugToolStripMenuItem"
        Me.BugToolStripMenuItem.Size = New System.Drawing.Size(75, 43)
        Me.BugToolStripMenuItem.Text = "Bug"
        '
        'StopToolStripMenuItem1
        '
        Me.StopToolStripMenuItem1.Name = "StopToolStripMenuItem1"
        Me.StopToolStripMenuItem1.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.Space), System.Windows.Forms.Keys)
        Me.StopToolStripMenuItem1.Size = New System.Drawing.Size(377, 42)
        Me.StopToolStripMenuItem1.Text = "Stop"
        '
        'WForwardToolStripMenuItem
        '
        Me.WForwardToolStripMenuItem.Name = "WForwardToolStripMenuItem"
        Me.WForwardToolStripMenuItem.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.W), System.Windows.Forms.Keys)
        Me.WForwardToolStripMenuItem.Size = New System.Drawing.Size(377, 42)
        Me.WForwardToolStripMenuItem.Text = "W Forward"
        '
        'WReverseToolStripMenuItem
        '
        Me.WReverseToolStripMenuItem.Name = "WReverseToolStripMenuItem"
        Me.WReverseToolStripMenuItem.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.Z), System.Windows.Forms.Keys)
        Me.WReverseToolStripMenuItem.Size = New System.Drawing.Size(377, 42)
        Me.WReverseToolStripMenuItem.Text = "W Reverse"
        '
        'WStationaryToolStripMenuItem
        '
        Me.WStationaryToolStripMenuItem.Name = "WStationaryToolStripMenuItem"
        Me.WStationaryToolStripMenuItem.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.S), System.Windows.Forms.Keys)
        Me.WStationaryToolStripMenuItem.Size = New System.Drawing.Size(377, 42)
        Me.WStationaryToolStripMenuItem.Text = "W Stationary"
        '
        'WSideLeftToolStripMenuItem
        '
        Me.WSideLeftToolStripMenuItem.Name = "WSideLeftToolStripMenuItem"
        Me.WSideLeftToolStripMenuItem.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.A), System.Windows.Forms.Keys)
        Me.WSideLeftToolStripMenuItem.Size = New System.Drawing.Size(377, 42)
        Me.WSideLeftToolStripMenuItem.Text = "W Side Left"
        '
        'WSideRightToolStripMenuItem
        '
        Me.WSideRightToolStripMenuItem.Name = "WSideRightToolStripMenuItem"
        Me.WSideRightToolStripMenuItem.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.D), System.Windows.Forms.Keys)
        Me.WSideRightToolStripMenuItem.Size = New System.Drawing.Size(377, 42)
        Me.WSideRightToolStripMenuItem.Text = "W Side Right"
        '
        'WPivotLeftToolStripMenuItem
        '
        Me.WPivotLeftToolStripMenuItem.Name = "WPivotLeftToolStripMenuItem"
        Me.WPivotLeftToolStripMenuItem.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.Q), System.Windows.Forms.Keys)
        Me.WPivotLeftToolStripMenuItem.Size = New System.Drawing.Size(377, 42)
        Me.WPivotLeftToolStripMenuItem.Text = "W Pivot Left"
        '
        'WPivotRightToolStripMenuItem
        '
        Me.WPivotRightToolStripMenuItem.Name = "WPivotRightToolStripMenuItem"
        Me.WPivotRightToolStripMenuItem.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.E), System.Windows.Forms.Keys)
        Me.WPivotRightToolStripMenuItem.Size = New System.Drawing.Size(377, 42)
        Me.WPivotRightToolStripMenuItem.Text = "W Pivot Right"
        '
        'StandToolStripMenuItem
        '
        Me.StandToolStripMenuItem.Name = "StandToolStripMenuItem"
        Me.StandToolStripMenuItem.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.R), System.Windows.Forms.Keys)
        Me.StandToolStripMenuItem.Size = New System.Drawing.Size(377, 42)
        Me.StandToolStripMenuItem.Text = "Stand"
        '
        'SitToolStripMenuItem
        '
        Me.SitToolStripMenuItem.Name = "SitToolStripMenuItem"
        Me.SitToolStripMenuItem.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.F), System.Windows.Forms.Keys)
        Me.SitToolStripMenuItem.Size = New System.Drawing.Size(377, 42)
        Me.SitToolStripMenuItem.Text = "Sit"
        '
        'CommandToolStripMenuItem
        '
        Me.CommandToolStripMenuItem.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.RunToolStripMenuItem, Me.StopToolStripMenuItem, Me.ToolStripMenuItem1, Me.ScanToolStripMenuItem, Me.ScanClearToolStripMenuItem, Me.ToolStripMenuItem2, Me.ForwardToolStripMenuItem, Me.BackwardToolStripMenuItem, Me.TurnLeftToolStripMenuItem, Me.TurnRightToolStripMenuItem, Me.MarchLeftToolStripMenuItem, Me.MarchRightToolStripMenuItem, Me.StopToolStripMenuItem2, Me.MarchOnTheSpotToolStripMenuItem, Me.VictoryDanceToolStripMenuItem, Me.StabToolStripMenuItem})
        Me.CommandToolStripMenuItem.Name = "CommandToolStripMenuItem"
        Me.CommandToolStripMenuItem.Size = New System.Drawing.Size(153, 43)
        Me.CommandToolStripMenuItem.Text = "Command"
        '
        'RunToolStripMenuItem
        '
        Me.RunToolStripMenuItem.Name = "RunToolStripMenuItem"
        Me.RunToolStripMenuItem.ShortcutKeys = System.Windows.Forms.Keys.F5
        Me.RunToolStripMenuItem.Size = New System.Drawing.Size(449, 42)
        Me.RunToolStripMenuItem.Text = "Run"
        '
        'StopToolStripMenuItem
        '
        Me.StopToolStripMenuItem.Name = "StopToolStripMenuItem"
        Me.StopToolStripMenuItem.Size = New System.Drawing.Size(449, 42)
        Me.StopToolStripMenuItem.Text = "Stop"
        '
        'ToolStripMenuItem1
        '
        Me.ToolStripMenuItem1.Name = "ToolStripMenuItem1"
        Me.ToolStripMenuItem1.Size = New System.Drawing.Size(446, 6)
        '
        'ScanToolStripMenuItem
        '
        Me.ScanToolStripMenuItem.Name = "ScanToolStripMenuItem"
        Me.ScanToolStripMenuItem.ShortcutKeys = System.Windows.Forms.Keys.F1
        Me.ScanToolStripMenuItem.Size = New System.Drawing.Size(449, 42)
        Me.ScanToolStripMenuItem.Text = "Scan"
        '
        'ScanClearToolStripMenuItem
        '
        Me.ScanClearToolStripMenuItem.Name = "ScanClearToolStripMenuItem"
        Me.ScanClearToolStripMenuItem.ShortcutKeys = System.Windows.Forms.Keys.F2
        Me.ScanClearToolStripMenuItem.Size = New System.Drawing.Size(449, 42)
        Me.ScanClearToolStripMenuItem.Text = "Scan Clear"
        '
        'ToolStripMenuItem2
        '
        Me.ToolStripMenuItem2.Name = "ToolStripMenuItem2"
        Me.ToolStripMenuItem2.Size = New System.Drawing.Size(446, 6)
        '
        'ForwardToolStripMenuItem
        '
        Me.ForwardToolStripMenuItem.Name = "ForwardToolStripMenuItem"
        Me.ForwardToolStripMenuItem.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.F), System.Windows.Forms.Keys)
        Me.ForwardToolStripMenuItem.Size = New System.Drawing.Size(449, 42)
        Me.ForwardToolStripMenuItem.Text = "Forward"
        '
        'BackwardToolStripMenuItem
        '
        Me.BackwardToolStripMenuItem.Name = "BackwardToolStripMenuItem"
        Me.BackwardToolStripMenuItem.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.B), System.Windows.Forms.Keys)
        Me.BackwardToolStripMenuItem.Size = New System.Drawing.Size(449, 42)
        Me.BackwardToolStripMenuItem.Text = "Backward"
        '
        'TurnLeftToolStripMenuItem
        '
        Me.TurnLeftToolStripMenuItem.Name = "TurnLeftToolStripMenuItem"
        Me.TurnLeftToolStripMenuItem.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.L), System.Windows.Forms.Keys)
        Me.TurnLeftToolStripMenuItem.Size = New System.Drawing.Size(449, 42)
        Me.TurnLeftToolStripMenuItem.Text = "Turn Left"
        '
        'TurnRightToolStripMenuItem
        '
        Me.TurnRightToolStripMenuItem.Name = "TurnRightToolStripMenuItem"
        Me.TurnRightToolStripMenuItem.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.R), System.Windows.Forms.Keys)
        Me.TurnRightToolStripMenuItem.Size = New System.Drawing.Size(449, 42)
        Me.TurnRightToolStripMenuItem.Text = "Turn Right"
        '
        'MarchLeftToolStripMenuItem
        '
        Me.MarchLeftToolStripMenuItem.Name = "MarchLeftToolStripMenuItem"
        Me.MarchLeftToolStripMenuItem.ShortcutKeys = CType(((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.Shift) _
            Or System.Windows.Forms.Keys.L), System.Windows.Forms.Keys)
        Me.MarchLeftToolStripMenuItem.Size = New System.Drawing.Size(449, 42)
        Me.MarchLeftToolStripMenuItem.Text = "March Left"
        '
        'MarchRightToolStripMenuItem
        '
        Me.MarchRightToolStripMenuItem.Name = "MarchRightToolStripMenuItem"
        Me.MarchRightToolStripMenuItem.ShortcutKeys = CType(((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.Shift) _
            Or System.Windows.Forms.Keys.R), System.Windows.Forms.Keys)
        Me.MarchRightToolStripMenuItem.Size = New System.Drawing.Size(449, 42)
        Me.MarchRightToolStripMenuItem.Text = "March Right"
        '
        'StopToolStripMenuItem2
        '
        Me.StopToolStripMenuItem2.Name = "StopToolStripMenuItem2"
        Me.StopToolStripMenuItem2.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.S), System.Windows.Forms.Keys)
        Me.StopToolStripMenuItem2.Size = New System.Drawing.Size(449, 42)
        Me.StopToolStripMenuItem2.Text = "Stop"
        '
        'MarchOnTheSpotToolStripMenuItem
        '
        Me.MarchOnTheSpotToolStripMenuItem.Name = "MarchOnTheSpotToolStripMenuItem"
        Me.MarchOnTheSpotToolStripMenuItem.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.O), System.Windows.Forms.Keys)
        Me.MarchOnTheSpotToolStripMenuItem.Size = New System.Drawing.Size(449, 42)
        Me.MarchOnTheSpotToolStripMenuItem.Text = "March On The Spot"
        '
        'VictoryDanceToolStripMenuItem
        '
        Me.VictoryDanceToolStripMenuItem.Name = "VictoryDanceToolStripMenuItem"
        Me.VictoryDanceToolStripMenuItem.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.V), System.Windows.Forms.Keys)
        Me.VictoryDanceToolStripMenuItem.Size = New System.Drawing.Size(449, 42)
        Me.VictoryDanceToolStripMenuItem.Text = "Victory Dance"
        '
        'StabToolStripMenuItem
        '
        Me.StabToolStripMenuItem.Name = "StabToolStripMenuItem"
        Me.StabToolStripMenuItem.ShortcutKeys = CType(((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.Shift) _
            Or System.Windows.Forms.Keys.S), System.Windows.Forms.Keys)
        Me.StabToolStripMenuItem.Size = New System.Drawing.Size(449, 42)
        Me.StabToolStripMenuItem.Text = "Stab"
        '
        'ToolStrip1
        '
        Me.ToolStrip1.AutoSize = False
        Me.ToolStrip1.ImageScalingSize = New System.Drawing.Size(32, 32)
        Me.ToolStrip1.Items.AddRange(New System.Windows.Forms.ToolStripItem() {Me.ToolStripButton1, Me.ToolStripComboBox1, Me.ToolStripSeparator1, Me.ToolStripButton3, Me.ToolStripButton2, Me.ToolStripButton4, Me.ToolStripButton5, Me.ToolStripSeparator2, Me.ToolStripTextBox1})
        Me.ToolStrip1.Location = New System.Drawing.Point(0, 51)
        Me.ToolStrip1.Name = "ToolStrip1"
        Me.ToolStrip1.Padding = New System.Windows.Forms.Padding(0, 0, 2, 0)
        Me.ToolStrip1.Size = New System.Drawing.Size(1754, 46)
        Me.ToolStrip1.TabIndex = 2
        Me.ToolStrip1.Text = "ToolStrip1"
        '
        'ToolStripButton1
        '
        Me.ToolStripButton1.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.ToolStripButton1.Image = CType(resources.GetObject("ToolStripButton1.Image"), System.Drawing.Image)
        Me.ToolStripButton1.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.ToolStripButton1.Name = "ToolStripButton1"
        Me.ToolStripButton1.Size = New System.Drawing.Size(36, 43)
        Me.ToolStripButton1.Text = "ToolStripButton1"
        '
        'ToolStripComboBox1
        '
        Me.ToolStripComboBox1.Name = "ToolStripComboBox1"
        Me.ToolStripComboBox1.Size = New System.Drawing.Size(277, 46)
        '
        'ToolStripSeparator1
        '
        Me.ToolStripSeparator1.Name = "ToolStripSeparator1"
        Me.ToolStripSeparator1.Size = New System.Drawing.Size(6, 46)
        '
        'ToolStripButton3
        '
        Me.ToolStripButton3.Alignment = System.Windows.Forms.ToolStripItemAlignment.Right
        Me.ToolStripButton3.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.ToolStripButton3.Image = CType(resources.GetObject("ToolStripButton3.Image"), System.Drawing.Image)
        Me.ToolStripButton3.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.ToolStripButton3.Name = "ToolStripButton3"
        Me.ToolStripButton3.Size = New System.Drawing.Size(36, 43)
        Me.ToolStripButton3.Text = "ToolStripButton3"
        '
        'ToolStripButton2
        '
        Me.ToolStripButton2.Alignment = System.Windows.Forms.ToolStripItemAlignment.Right
        Me.ToolStripButton2.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.ToolStripButton2.Image = CType(resources.GetObject("ToolStripButton2.Image"), System.Drawing.Image)
        Me.ToolStripButton2.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.ToolStripButton2.Name = "ToolStripButton2"
        Me.ToolStripButton2.Size = New System.Drawing.Size(36, 43)
        Me.ToolStripButton2.Text = "ToolStripButton2"
        '
        'ToolStripButton4
        '
        Me.ToolStripButton4.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.ToolStripButton4.Image = CType(resources.GetObject("ToolStripButton4.Image"), System.Drawing.Image)
        Me.ToolStripButton4.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.ToolStripButton4.Name = "ToolStripButton4"
        Me.ToolStripButton4.Size = New System.Drawing.Size(36, 43)
        Me.ToolStripButton4.Text = "ToolStripButton4"
        '
        'ToolStripButton5
        '
        Me.ToolStripButton5.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        Me.ToolStripButton5.Image = CType(resources.GetObject("ToolStripButton5.Image"), System.Drawing.Image)
        Me.ToolStripButton5.ImageTransparentColor = System.Drawing.Color.Magenta
        Me.ToolStripButton5.Name = "ToolStripButton5"
        Me.ToolStripButton5.Size = New System.Drawing.Size(36, 43)
        Me.ToolStripButton5.Text = "ToolStripButton5"
        '
        'ToolStripSeparator2
        '
        Me.ToolStripSeparator2.Name = "ToolStripSeparator2"
        Me.ToolStripSeparator2.Size = New System.Drawing.Size(6, 46)
        '
        'ToolStripTextBox1
        '
        Me.ToolStripTextBox1.Name = "ToolStripTextBox1"
        Me.ToolStripTextBox1.Size = New System.Drawing.Size(228, 46)
        '
        'BackgroundWorker1
        '
        '
        'ImageList1
        '
        Me.ImageList1.ColorDepth = System.Windows.Forms.ColorDepth.Depth8Bit
        Me.ImageList1.ImageSize = New System.Drawing.Size(16, 16)
        Me.ImageList1.TransparentColor = System.Drawing.Color.Transparent
        '
        'Button1
        '
        Me.Button1.Location = New System.Drawing.Point(787, 188)
        Me.Button1.Margin = New System.Windows.Forms.Padding(7)
        Me.Button1.Name = "Button1"
        Me.Button1.Size = New System.Drawing.Size(218, 119)
        Me.Button1.TabIndex = 3
        Me.Button1.Text = "Stand"
        Me.Button1.UseVisualStyleBackColor = True
        '
        'Button2
        '
        Me.Button2.Location = New System.Drawing.Point(1308, 188)
        Me.Button2.Margin = New System.Windows.Forms.Padding(7)
        Me.Button2.Name = "Button2"
        Me.Button2.Size = New System.Drawing.Size(218, 119)
        Me.Button2.TabIndex = 5
        Me.Button2.Text = "Sit"
        Me.Button2.UseVisualStyleBackColor = True
        '
        'DebugW
        '
        Me.DebugW.Dock = System.Windows.Forms.DockStyle.Left
        Me.DebugW.Location = New System.Drawing.Point(0, 97)
        Me.DebugW.Margin = New System.Windows.Forms.Padding(7)
        Me.DebugW.Multiline = True
        Me.DebugW.Name = "DebugW"
        Me.DebugW.Size = New System.Drawing.Size(702, 925)
        Me.DebugW.TabIndex = 7
        '
        'TextBox3
        '
        Me.TextBox3.Location = New System.Drawing.Point(1498, 858)
        Me.TextBox3.Margin = New System.Windows.Forms.Padding(7)
        Me.TextBox3.Name = "TextBox3"
        Me.TextBox3.Size = New System.Drawing.Size(130, 35)
        Me.TextBox3.TabIndex = 8
        Me.TextBox3.Text = "300"
        '
        'Button3
        '
        Me.Button3.Location = New System.Drawing.Point(1050, 321)
        Me.Button3.Margin = New System.Windows.Forms.Padding(7)
        Me.Button3.Name = "Button3"
        Me.Button3.Size = New System.Drawing.Size(218, 119)
        Me.Button3.TabIndex = 9
        Me.Button3.Text = "March On The Spot"
        Me.Button3.UseVisualStyleBackColor = True
        '
        'Button4
        '
        Me.Button4.Location = New System.Drawing.Point(1050, 455)
        Me.Button4.Margin = New System.Windows.Forms.Padding(7)
        Me.Button4.Name = "Button4"
        Me.Button4.Size = New System.Drawing.Size(218, 119)
        Me.Button4.TabIndex = 10
        Me.Button4.Text = "Stop"
        Me.Button4.UseVisualStyleBackColor = True
        '
        'Button5
        '
        Me.Button5.Location = New System.Drawing.Point(1050, 588)
        Me.Button5.Margin = New System.Windows.Forms.Padding(7)
        Me.Button5.Name = "Button5"
        Me.Button5.Size = New System.Drawing.Size(218, 124)
        Me.Button5.TabIndex = 11
        Me.Button5.Text = "Backward"
        Me.Button5.UseVisualStyleBackColor = True
        '
        'Button6
        '
        Me.Button6.Location = New System.Drawing.Point(1050, 188)
        Me.Button6.Margin = New System.Windows.Forms.Padding(7)
        Me.Button6.Name = "Button6"
        Me.Button6.Size = New System.Drawing.Size(218, 119)
        Me.Button6.TabIndex = 12
        Me.Button6.Text = "Forward"
        Me.Button6.UseVisualStyleBackColor = True
        '
        'Button7
        '
        Me.Button7.Location = New System.Drawing.Point(1308, 455)
        Me.Button7.Margin = New System.Windows.Forms.Padding(7)
        Me.Button7.Name = "Button7"
        Me.Button7.Size = New System.Drawing.Size(218, 119)
        Me.Button7.TabIndex = 13
        Me.Button7.Text = "March Right"
        Me.Button7.UseVisualStyleBackColor = True
        '
        'Button8
        '
        Me.Button8.Cursor = System.Windows.Forms.Cursors.No
        Me.Button8.Location = New System.Drawing.Point(787, 455)
        Me.Button8.Margin = New System.Windows.Forms.Padding(7)
        Me.Button8.Name = "Button8"
        Me.Button8.Size = New System.Drawing.Size(218, 119)
        Me.Button8.TabIndex = 14
        Me.Button8.Text = "March Left"
        Me.Button8.UseVisualStyleBackColor = True
        '
        'Button9
        '
        Me.Button9.Location = New System.Drawing.Point(787, 321)
        Me.Button9.Margin = New System.Windows.Forms.Padding(7)
        Me.Button9.Name = "Button9"
        Me.Button9.Size = New System.Drawing.Size(218, 119)
        Me.Button9.TabIndex = 15
        Me.Button9.Text = "Turn Left"
        Me.Button9.UseVisualStyleBackColor = True
        '
        'Button10
        '
        Me.Button10.Location = New System.Drawing.Point(1308, 321)
        Me.Button10.Margin = New System.Windows.Forms.Padding(7)
        Me.Button10.Name = "Button10"
        Me.Button10.Size = New System.Drawing.Size(218, 119)
        Me.Button10.TabIndex = 16
        Me.Button10.Text = "Turn Right"
        Me.Button10.UseVisualStyleBackColor = True
        '
        'TextBox4
        '
        Me.TextBox4.Location = New System.Drawing.Point(1498, 916)
        Me.TextBox4.Margin = New System.Windows.Forms.Padding(7)
        Me.TextBox4.Name = "TextBox4"
        Me.TextBox4.Size = New System.Drawing.Size(130, 35)
        Me.TextBox4.TabIndex = 18
        Me.TextBox4.Text = "40"
        '
        'TextBox5
        '
        Me.TextBox5.Location = New System.Drawing.Point(1498, 974)
        Me.TextBox5.Margin = New System.Windows.Forms.Padding(7)
        Me.TextBox5.Name = "TextBox5"
        Me.TextBox5.Size = New System.Drawing.Size(130, 35)
        Me.TextBox5.TabIndex = 19
        Me.TextBox5.Text = "50"
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(1329, 862)
        Me.Label1.Margin = New System.Windows.Forms.Padding(7, 0, 7, 0)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(146, 29)
        Me.Label1.TabIndex = 20
        Me.Label1.Text = "Speed (150)"
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Location = New System.Drawing.Point(1398, 920)
        Me.Label2.Margin = New System.Windows.Forms.Padding(7, 0, 7, 0)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(80, 29)
        Me.Label2.TabIndex = 21
        Me.Label2.Text = "Swing"
        '
        'Label3
        '
        Me.Label3.AutoSize = True
        Me.Label3.Location = New System.Drawing.Point(1309, 978)
        Me.Label3.Margin = New System.Windows.Forms.Padding(7, 0, 7, 0)
        Me.Label3.Name = "Label3"
        Me.Label3.Size = New System.Drawing.Size(168, 29)
        Me.Label3.TabIndex = 22
        Me.Label3.Text = "TurningSpeed"
        '
        'Button12
        '
        Me.Button12.Location = New System.Drawing.Point(787, 588)
        Me.Button12.Name = "Button12"
        Me.Button12.Size = New System.Drawing.Size(218, 128)
        Me.Button12.TabIndex = 23
        Me.Button12.Text = "Victory Dance"
        Me.Button12.UseVisualStyleBackColor = True
        '
        'TextBox2
        '
        Me.TextBox2.Location = New System.Drawing.Point(1308, 126)
        Me.TextBox2.Margin = New System.Windows.Forms.Padding(7)
        Me.TextBox2.Name = "TextBox2"
        Me.TextBox2.Size = New System.Drawing.Size(217, 35)
        Me.TextBox2.TabIndex = 6
        Me.TextBox2.Text = "300"
        '
        'TextBox1
        '
        Me.TextBox1.Location = New System.Drawing.Point(787, 126)
        Me.TextBox1.Margin = New System.Windows.Forms.Padding(7)
        Me.TextBox1.Name = "TextBox1"
        Me.TextBox1.Size = New System.Drawing.Size(217, 35)
        Me.TextBox1.TabIndex = 4
        Me.TextBox1.Text = "511"
        '
        'Button13
        '
        Me.Button13.Location = New System.Drawing.Point(1307, 594)
        Me.Button13.Name = "Button13"
        Me.Button13.Size = New System.Drawing.Size(219, 122)
        Me.Button13.TabIndex = 25
        Me.Button13.Text = "Stab"
        Me.Button13.UseVisualStyleBackColor = True
        '
        'FMain
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(14.0!, 29.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(1754, 1064)
        Me.Controls.Add(Me.Button13)
        Me.Controls.Add(Me.Button12)
        Me.Controls.Add(Me.Label3)
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.Label1)
        Me.Controls.Add(Me.TextBox5)
        Me.Controls.Add(Me.TextBox4)
        Me.Controls.Add(Me.Button10)
        Me.Controls.Add(Me.Button9)
        Me.Controls.Add(Me.Button8)
        Me.Controls.Add(Me.Button7)
        Me.Controls.Add(Me.Button6)
        Me.Controls.Add(Me.Button5)
        Me.Controls.Add(Me.Button4)
        Me.Controls.Add(Me.Button3)
        Me.Controls.Add(Me.TextBox3)
        Me.Controls.Add(Me.DebugW)
        Me.Controls.Add(Me.TextBox2)
        Me.Controls.Add(Me.Button2)
        Me.Controls.Add(Me.TextBox1)
        Me.Controls.Add(Me.Button1)
        Me.Controls.Add(Me.ToolStrip1)
        Me.Controls.Add(Me.StatusStrip1)
        Me.Controls.Add(Me.MenuStrip1)
        Me.MainMenuStrip = Me.MenuStrip1
        Me.Margin = New System.Windows.Forms.Padding(7)
        Me.Name = "FMain"
        Me.Text = "DigiS 6Legged"
        Me.StatusStrip1.ResumeLayout(False)
        Me.StatusStrip1.PerformLayout()
        Me.MenuStrip1.ResumeLayout(False)
        Me.MenuStrip1.PerformLayout()
        Me.ToolStrip1.ResumeLayout(False)
        Me.ToolStrip1.PerformLayout()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents SerialPort1 As System.IO.Ports.SerialPort
    Friend WithEvents StatusStrip1 As System.Windows.Forms.StatusStrip
    Friend WithEvents MenuStrip1 As System.Windows.Forms.MenuStrip
    Friend WithEvents FileToolStripMenuItem As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents CloseToolStripMenuItem As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents ToolStrip1 As System.Windows.Forms.ToolStrip
    Friend WithEvents ToolStripComboBox1 As System.Windows.Forms.ToolStripComboBox
    Friend WithEvents ToolStripStatusLabel1 As System.Windows.Forms.ToolStripStatusLabel
    Friend WithEvents ToolStripButton1 As System.Windows.Forms.ToolStripButton
    Friend WithEvents BackgroundWorker1 As System.ComponentModel.BackgroundWorker
    Friend WithEvents ToolStripSeparator1 As System.Windows.Forms.ToolStripSeparator
    Friend WithEvents ToolStripButton2 As System.Windows.Forms.ToolStripButton
    Friend WithEvents CommandToolStripMenuItem As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents RunToolStripMenuItem As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents StopToolStripMenuItem As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents ToolStripButton3 As System.Windows.Forms.ToolStripButton
    Friend WithEvents ImageList1 As System.Windows.Forms.ImageList
    Friend WithEvents Button1 As System.Windows.Forms.Button
    Friend WithEvents Button2 As System.Windows.Forms.Button
    Friend WithEvents DebugW As System.Windows.Forms.TextBox
    Friend WithEvents ToolStripButton4 As System.Windows.Forms.ToolStripButton
    Friend WithEvents TextBox3 As System.Windows.Forms.TextBox
    Friend WithEvents ToolStripButton5 As System.Windows.Forms.ToolStripButton
    Friend WithEvents ToolStripSeparator2 As System.Windows.Forms.ToolStripSeparator
    Friend WithEvents ToolStripTextBox1 As System.Windows.Forms.ToolStripTextBox
    Friend WithEvents ToolStripMenuItem1 As System.Windows.Forms.ToolStripSeparator
    Friend WithEvents ScanToolStripMenuItem As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents ScanClearToolStripMenuItem As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents Button3 As System.Windows.Forms.Button
    Friend WithEvents Button4 As System.Windows.Forms.Button
    Friend WithEvents Button5 As System.Windows.Forms.Button
    Friend WithEvents Button6 As System.Windows.Forms.Button
    Friend WithEvents Button7 As System.Windows.Forms.Button
    Friend WithEvents Button8 As System.Windows.Forms.Button
    Friend WithEvents Button9 As System.Windows.Forms.Button
    Friend WithEvents Button10 As System.Windows.Forms.Button
    Friend WithEvents BugToolStripMenuItem As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents StopToolStripMenuItem1 As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents WForwardToolStripMenuItem As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents WReverseToolStripMenuItem As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents WStationaryToolStripMenuItem As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents WSideLeftToolStripMenuItem As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents WSideRightToolStripMenuItem As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents WPivotLeftToolStripMenuItem As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents WPivotRightToolStripMenuItem As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents StandToolStripMenuItem As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents SitToolStripMenuItem As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents TextBox4 As System.Windows.Forms.TextBox
    Friend WithEvents TextBox5 As System.Windows.Forms.TextBox
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents Label2 As System.Windows.Forms.Label
    Friend WithEvents Label3 As System.Windows.Forms.Label
    Friend WithEvents Button12 As Button
    Friend WithEvents ToolStripMenuItem2 As ToolStripSeparator
    Friend WithEvents ForwardToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents BackwardToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents TurnLeftToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents TurnRightToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents MarchLeftToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents MarchRightToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents StopToolStripMenuItem2 As ToolStripMenuItem
    Friend WithEvents MarchOnTheSpotToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents VictoryDanceToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents TextBox2 As TextBox
    Friend WithEvents TextBox1 As TextBox
    Friend WithEvents Button13 As Button
    Friend WithEvents StabToolStripMenuItem As ToolStripMenuItem
End Class
