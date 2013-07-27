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
        
        self.layoutWidgets()
        
    #----------------------------------------------------------------------
    def layoutWidgets(self):
        """
        Create and layout the widgets
        """
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.fgSizer = wx.FlexGridSizer(rows=3, cols=3, vgap=5, hgap=5)
                
        widgets = []
        size = (100,100)
        for item in range(9):
            name = "toggle%s" % (item+1)
            button = buttons.GenToggleButton(self, size=size, name=name)
            button.Bind(wx.EVT_BUTTON, self.onToggle)
            widgets.append(button)
            
        self.fgSizer.AddMany(widgets)
        mainSizer.Add(self.fgSizer, 0, wx.ALL|wx.CENTER, 5)
        
        endTurnBtn = wx.Button(self, label="End Turn")
        mainSizer.Add(endTurnBtn, 0, wx.ALL|wx.CENTER, 5)
        
        self.SetSizer(mainSizer)
        
    #----------------------------------------------------------------------
    def onToggle(self, event):
        """
        On button toggle, change the label of the button pressed
        and disable the other buttons unless the user changes their mind
        """
        button = event.GetEventObject()
        button.SetLabel("X")
        button_name = button.GetName()
        
        items = self.fgSizer.GetChildren()
        for item in items:
            btn = item.GetWindow()
            if button_name != btn.GetName():
                btn.Disable()
            else:
                btn.SetLabel("")
            
        print
    
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
    
    