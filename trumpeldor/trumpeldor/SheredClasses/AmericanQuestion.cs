using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using Xamarin.Forms;

namespace trumpeldor.SheredClasses
{
	public class AmericanQuestion
    {
        public int id { get; set; }
        public string question { get; set; }
        public List<string> answers { get; set; }
        public int indexOfCorrectAnswer { get; set; }

        //protected override void addToLayout(StackLayout layout)
        //{
        //    Button b1=new Button();
        //    b1.Text = "kaki";
        //    Button b2 = new Button();
        //    b2.Text = "kaki1";
        //    Button b3 = new Button();
        //    b3.Text = "kaki3";



        //    layout.Children.Add(b1);
        //    layout.Children.Add(b2);
        //    layout.Children.Add(b3);

        //}

        public void func()
        {
            
        }
    }
}