using System;
using System.Collections.Generic;
using System.Text;
using Xamarin.Forms;

namespace trumpeldor.SheredClasses
{
    public class VideoClue : Clue
    {
        public void addToLayout(StackLayout layout)
        {
            //TODO- not video
            Label label = new Label();
            label.Text = "new clue";
            layout.Children.Add(label);
        }
    }
}
