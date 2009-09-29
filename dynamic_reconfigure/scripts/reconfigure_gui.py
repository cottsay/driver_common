#! /usr/bin/env python
#***********************************************************
#* Software License Agreement (BSD License)
#*
#*  Copyright (c) 2009, Willow Garage, Inc.
#*  All rights reserved.
#*
#*  Redistribution and use in source and binary forms, with or without
#*  modification, are permitted provided that the following conditions
#*  are met:
#*
#*   * Redistributions of source code must retain the above copyright
#*     notice, this list of conditions and the following disclaimer.
#*   * Redistributions in binary form must reproduce the above
#*     copyright notice, this list of conditions and the following
#*     disclaimer in the documentation and/or other materials provided
#*     with the distribution.
#*   * Neither the name of the Willow Garage nor the names of its
#*     contributors may be used to endorse or promote products derived
#*     from this software without specific prior written permission.
#*
#*  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#*  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#*  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
#*  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
#*  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
#*  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
#*  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#*  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#*  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
#*  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
#*  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#*  POSSIBILITY OF SUCH DAMAGE.
#***********************************************************


import roslib; roslib.load_manifest('dynamic_reconfigure')
import rospy
import dynamic_reconfigure.dynamic_reconfigure as dynamic_reconfigure
import wx

class DynamicReconfigurePanel(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(200,100))
        self.control = wx.TextCtrl(self, 1, style=wx.TE_MULTILINE)
        self.Show(True)

class MainWindow(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, wx.ID_ANY, title)
        self.filemenu = wx.Menu()
        self.filemenu.Append(wx.ID_EXIT, "E&xit"," Exit the program")
        self.menubar = wx.MenuBar()
        self.menubar.Append(self.filemenu,"&File")
        self.SetMenuBar(self.menubar)
        wx.EVT_MENU(self, wx.ID_EXIT, self.on_exit)
        
        sizer = wx.BoxSizer()
        self.SetSizer(sizer)
        sizer.Add(GripperPressurePanel(self, 'pressure/r_gripper_motor'), 1, wx.EXPAND)
        
        #self.SetMaxSize(wx.Size(1500,1500))

    def on_exit(self, e):
        self.Close(True)
            
    def on_error(self):
        self.Raise()
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame=DynamicReconfigurePanel(None, wx.ID_ANY, 'Small editor')
    app.MainLoop()