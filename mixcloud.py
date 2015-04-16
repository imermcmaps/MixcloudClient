import wx
import wx.html2
import win32con

class Mixcloud(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, "Loading...")
		self.browser = wx.html2.WebView.New(self)
		self.browser.LoadURL("https://mixcloud.com")
		self.Show()
		self.timer = wx.Timer(self, 100)
		self.timer.Start(500)
		wx.EVT_TIMER(self, 100, self.update)
		self.regHotKey()
		self.Bind(wx.EVT_HOTKEY, self.handlePlayKey, id=100)
		self.Bind(wx.EVT_HOTKEY, self.handleNextKey, id=101)
		self.Bind(wx.EVT_HOTKEY, self.handlePrevKey, id=102)
	def regHotKey(self):
		self.RegisterHotKey(100, 0, win32con.VK_MEDIA_PLAY_PAUSE)
		self.RegisterHotKey(101, 0, win32con.VK_MEDIA_NEXT_TRACK)
		self.RegisterHotKey(102, 0, win32con.VK_MEDIA_PREV_TRACK)
	def handlePlayKey(self, evt):
		self.browser.RunScript("$('.player-control').click();")
	def handleNextKey(self, evt):
		self.browser.RunScript("$('.cloudcast-row.now-playing').next().find('.play-button-play').click();")
	def handlePrevKey(self, evt):
		self.browser.RunScript("$('.cloudcast-row.now-playing').prev().find('.play-button-play').click();")
	def update(self, e):
		title = self.browser.GetCurrentTitle()
		if title == "":
			return
		if not title.endswith(" | Mixcloud"):
			title += " | Mixcloud"

		self.SetTitle(title)


app = wx.App(False)
frame = Mixcloud()
app.MainLoop()
