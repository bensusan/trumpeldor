using System;
using System.Collections.Generic;
using System.Text;
using Xamarin.Forms;

namespace trumpeldor.SheredClasses
{
    public class TextClue : Clue
    {
        public TextClue()
        {

        }
        public void addToLayout(StackLayout layout)
        {
            Label label = new Label();
            label.Text = "new clue";
            layout.Children.Add(label);
        }

       


    }
}
