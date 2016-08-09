import wx

from functools import partial


class MainFrame(wx.Frame):
    """
    This app shows a group of buttons
    """

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super(MainFrame, self).__init__(parent=None, title='Partial')
        panel = wx.Panel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)
        btn_labels = ['one', 'two', 'three']
        for label in btn_labels:
            btn = wx.Button(panel, label=label)
            btn.Bind(wx.EVT_BUTTON, partial(self.onButton, label=label))
            sizer.Add(btn, 0, wx.ALL, 5)

        panel.SetSizer(sizer)
        self.Show()

    def onButton(self, event, label):
        """
        Event handler called when a button is pressed
        """
        print('You pressed: ' +  str(label))


if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()