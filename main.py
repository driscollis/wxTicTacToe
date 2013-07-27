import wx

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
    
    