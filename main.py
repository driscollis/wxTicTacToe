import wx
import wx.lib.buttons as buttons

########################################################################
class TTTPanel(wx.Panel):
    """
    Tic-Tac-Toe Panel object
    """

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """
        Initialize the panel
        """
        wx.Panel.__init__(self, parent)
        self.toggled = False
        
        self.layoutWidgets()
        
    #----------------------------------------------------------------------
    def checkWin(self, computer=False):
        """
        Check if the player won
        """
        for button1, button2, button3 in self.methodsToWin:
            if button1.GetLabel() == button2.GetLabel() and \
               button2.GetLabel() == button3.GetLabel() and \
               button1.GetLabel() != "":
                print "Player wins!"
                button1.SetBackgroundColour("Red")
                button2.SetBackgroundColour("Red")
                button3.SetBackgroundColour("Red")
                self.Layout()
                
                if not computer:
                    msg = "You Won!"
                    dlg = wx.MessageDialog(None, msg, "Winner!", wx.OK | wx.ICON_WARNING)
                    dlg.ShowModal()
                    dlg.Destroy()
                else:
                    return True
        
    #----------------------------------------------------------------------
    def layoutWidgets(self):
        """
        Create and layout the widgets
        """
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.fgSizer = wx.FlexGridSizer(rows=3, cols=3, vgap=5, hgap=5)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        font = wx.Font(22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                       wx.FONTWEIGHT_BOLD)
        
        size = (100,100)
        self.button1 = buttons.GenToggleButton(self, size=size)
        self.button2 = buttons.GenToggleButton(self, size=size)
        self.button3 = buttons.GenToggleButton(self, size=size)
        self.button4 = buttons.GenToggleButton(self, size=size)
        self.button5 = buttons.GenToggleButton(self, size=size)
        self.button6 = buttons.GenToggleButton(self, size=size)
        self.button7 = buttons.GenToggleButton(self, size=size)
        self.button8 = buttons.GenToggleButton(self, size=size)
        self.button9 = buttons.GenToggleButton(self, size=size)
        self.normalBtnColour = self.button1.GetBackgroundColour()
        
        self.widgets = [self.button1, self.button2, self.button3,
                        self.button4, self.button5, self.button6, 
                        self.button7, self.button8, self.button9]
        
        # change all the main game buttons' font and bind them to an event
        for button in self.widgets:
            button.SetFont(font)
            button.Bind(wx.EVT_BUTTON, self.onToggle)            
                    
        # add the widgets to the sizers
        self.fgSizer.AddMany(self.widgets)
        mainSizer.Add(self.fgSizer, 0, wx.ALL|wx.CENTER, 5)
        
        endTurnBtn = wx.Button(self, label="End Turn")
        endTurnBtn.Bind(wx.EVT_BUTTON, self.onEndTurn)
        btnSizer.Add(endTurnBtn, 0, wx.ALL|wx.CENTER, 5)
        
        startOverBtn = wx.Button(self, label="Restart")
        startOverBtn.Bind(wx.EVT_BUTTON, self.onRestart)
        btnSizer.Add(startOverBtn, 0, wx.ALL|wx.CENTER, 5)
        mainSizer.Add(btnSizer, 0, wx.CENTER)
        
        self.methodsToWin = [(self.button1, self.button2, self.button3),
                             (self.button4, self.button5, self.button6),
                             (self.button7, self.button8, self.button9),
                             # vertical ways to win
                             (self.button1, self.button4, self.button7),
                             (self.button2, self.button5, self.button8),
                             (self.button3, self.button6, self.button9),
                             # diagonal ways to win
                             (self.button1, self.button5, self.button9),
                             (self.button3, self.button5, self.button7)]
        
        self.SetSizer(mainSizer)
        
    #----------------------------------------------------------------------
    def enableUnusedButtons(self):
        """
        Re-enable unused buttons
        """
        for button in self.widgets:
            if button.GetLabel() == "":
                button.Enable()
        self.Refresh()
        self.Layout()
        
    #----------------------------------------------------------------------
    def onEndTurn(self, event):
        """
        Let the computer play
        """
        # rest toggled flag state
        self.toggled = False
        
        # disable all played buttons
        for btn in self.widgets:
            if btn.GetLabel():
                btn.Disable()
        
        computerPlays = []
        noPlays = []
        
        for button1, button2, button3 in self.methodsToWin:
            if button1.GetLabel() == button2.GetLabel() and button1.GetLabel() != "":
                if button1.GetLabel() == "O":
                    noPlays.append(button3)
                continue
            elif button1.GetLabel() == button3.GetLabel() and button1.GetLabel() != "":
                if button1.GetLabel() == "O":
                    noPlays.append(button3)
                continue
            if button1.GetLabel() == "" and button1 not in noPlays:
                if not self.checkWin(computer=True):
                    computerPlays.append(button1)
                    break
            if button2.GetLabel() == "" and button2 not in noPlays:
                if not self.checkWin(computer=True):
                    computerPlays.append(button2)
                    break
            if button3.GetLabel() == "" and button3 not in noPlays:
                if not self.checkWin(computer=True):
                    computerPlays.append(button3)
                    break
        
        print self.checkWin()
        computerPlays[0].SetLabel("O")
        computerPlays[0].Disable()
        
        self.enableUnusedButtons()
        
    #----------------------------------------------------------------------
    def onRestart(self, event):
        """
        Clear and re-enable all the buttons 
        """
        for button in self.widgets:
            button.SetLabel("")
            button.SetValue(False)
            button.SetBackgroundColour(self.normalBtnColour)
        self.toggled = False
        self.enableUnusedButtons()
                
    #----------------------------------------------------------------------
    def onToggle(self, event):
        """
        On button toggle, change the label of the button pressed
        and disable the other buttons unless the user changes their mind
        """
        button = event.GetEventObject()
        button.SetLabel("X")
        button_id = button.GetId()
        
        self.checkWin()
        if not self.toggled:
            self.toggled = True
            for btn in self.widgets:
                if button_id != btn.GetId():
                    btn.Disable()
        else:
            self.toggled = False
            button.SetLabel("")
            self.enableUnusedButtons()
            
########################################################################
class TTTFrame(wx.Frame):
    """
    Tic-Tac-Toe Frame object
    """

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        title = "Tic-Tac-Toe"
        size = (500, 500)
        wx.Frame.__init__(self, parent=None, title=title, size=size)
        panel = TTTPanel(self)
        
        self.Show()
        
if __name__ == "__main__":
    app = wx.App(False)
    frame = TTTFrame()
    app.MainLoop()
    
    