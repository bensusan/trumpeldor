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
            foreach(var btn in layout.Children)
            {
                if (btn is ImageButton)
                    ((ImageButton)btn).IsEnabled = false;
                else if (btn is Button)
                    ((Button)btn).IsEnabled = false;
            }
        }

        public static void UnlockAll(StackLayout layout)
        {
            foreach (var btn in layout.Children)
            {
                if (btn is ImageButton)
                    ((ImageButton)btn).IsEnabled = true;
                else if (btn is Button)
                    ((Button)btn).IsEnabled = true;
            }
        }
    }
}
