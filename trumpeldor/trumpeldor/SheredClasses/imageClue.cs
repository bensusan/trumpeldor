using System;
using System.Collections.Generic;
using System.Text;
using Xamarin.Forms;

namespace trumpeldor.SheredClasses
{
    public class ImageClue : Clue
    {
        public void addToLayout(StackLayout layout)
        {
            Image img = new Image();
            img.Source = ImageSource.FromResource("trumpeldor.Resources.MapIcon.png");
            layout.Children.Add(img);
        }
    }
}
