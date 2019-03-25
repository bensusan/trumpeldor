using System;
using System.Collections.Generic;
using System.Text;
using trumpeldor.Views;
using Xamarin.Forms;

namespace trumpeldor.SheredClasses
{
    public class SlidingPuzzle : Entertainment
    {
        //public override int id { get; set; }
        //public int id { get; set; }
        public List<string> piecesURLS { set; get; }
        public int width { get; set; }
        public int height { get; set; }

        public override string EntertainmentName()
        {
           return AppResources.sliding_puzzle;
        }

        public override ContentPage EntertainmentPageInstance(ContentPage nextPage)
        {
            return new SlidingPuzzlePage(this, nextPage);
        }

        public static bool isMyClassName(string className)
        {
            return "SlidingPuzzle".Equals(className);
        }
    }
}
