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
        fgSizer = wx.FlexGridSizer(rows=3, cols=3, vgap=5, hgap=5)
        
        widgets = []
        size = (100,100)
        for item in range(9):
            name = "toggle%s" % (item+1)
            button = buttons.GenToggleButton(self, size=size, name=name)
            widgets.append(button)
            
        fgSizer.AddMany(widgets)
        mainSizer.Add(fgSizer, 0, wx.ALL|wx.CENTER, 5)
        
        endTurnBtn = wx.Button(self, label="End Turn")
        mainSizer.Add(endTurnBtn, 0, wx.ALL|wx.CENTER, 5)
        
        self.SetSizer(mainSizer)
    
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
    
    