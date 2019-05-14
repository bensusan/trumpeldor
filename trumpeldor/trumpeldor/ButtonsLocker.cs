using System;
using System.Collections.Generic;
using System.Text;
using Xamarin.Forms;

namespace trumpeldor
{
    public static class ButtonsLocker
    {
        public static void LockAll(StackLayout layout)
        {
            foreach(Button btn in layout.Children)
            {
                btn.IsEnabled = false;
            }
        }

        public static void UnlockAll(StackLayout layout)
        {
            foreach (Button btn in layout.Children)
            {
                btn.IsEnabled = true;
            }
        }
    }
}
