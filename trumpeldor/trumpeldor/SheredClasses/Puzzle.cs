using System;
using System.Collections.Generic;
using System.Text;
using trumpeldor.Views;
using Xamarin.Forms;

namespace trumpeldor.SheredClasses
{
    public class Puzzle : Entertainment
    {
        public List<string> piecesURLS { set; get; }
        public int width { get; set; }
        public int height { get; set; }

        public override string EntertainmentName()
        {
            return AppResources.puzzle;
        }

        public override ContentPage EntertainmentPageInstance(Attraction attraction)
        {
            return new JigsawPuzzlePage(this, attraction);
        }

        public static bool isMyClassName(string className)
        {
            return "Puzzle".Equals(className);
        }
    }
}
