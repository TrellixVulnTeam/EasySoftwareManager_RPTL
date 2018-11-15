﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class WindowRegister : Singleton<WindowRegister>{

    public override void Init()
    {
        base.Init();

        WindowManager mgr = WindowManager.Instance;

        mgr.RegisterWindow(WinNames.Test_Panel, new TestPanel());

    }
}