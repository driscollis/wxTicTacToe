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
    def layoutWidgets(self):
        """
        Create and layout the widgets
        """
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.fgSizer = wx.FlexGridSizer(rows=3, cols=3, vgap=5, hgap=5)
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
        self.widgets = [self.button1, self.button2, self.button3,
                        self.button4, self.button5, self.button6, 
                        self.button7, self.button8, self.button9]
        for button in self.widgets:
            button.SetFont(font)
            button.Bind(wx.EVT_BUTTON, self.onToggle)            
                    
        self.fgSizer.AddMany(self.widgets)
        mainSizer.Add(self.fgSizer, 0, wx.ALL|wx.CENTER, 5)
        
        endTurnBtn = wx.Button(self, label="End Turn")
        mainSizer.Add(endTurnBtn, 0, wx.ALL|wx.CENTER, 5)
        
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
        """
        pass
                
    #----------------------------------------------------------------------
    def onToggle(self, event):
        """
        On button toggle, change the label of the button pressed
        and disable the other buttons unless the user changes their mind
        """
        button = event.GetEventObject()
        button.SetLabel("X")
        button_id = button.GetId()
        #print "you pressed " + button_name

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
    
    