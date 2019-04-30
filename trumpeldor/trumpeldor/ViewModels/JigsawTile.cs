using System;
using System.Collections.Generic;
using System.Text;
using Xamarin.Forms;

namespace trumpeldor.ViewModels
{
    class JigsawTile
    {
        //const string UrlPrefix = "http://xamarin.github.io/xamarin-forms-book-samples/XamagonXuzzle/";

        public static Dictionary<View, JigsawTile> Dictionary { get; } = new Dictionary<View, JigsawTile>();

        public int correctRow { set; get; }

        public int correctCol { set; get; }

        public bool isSetOnPossition { set; get; }

        public View TileView { private set; get; }

        public double lastKnownX { get; set; }

        public double lastKnownY { get; set; }

        public JigsawTile(int row, int col, string pictureName)
        {
            correctRow = row;
            correctCol = col;

            TileView = new ContentView
            {
                Padding = new Thickness(1),
                Content = new Image { Source = ImageSource.FromUri(new Uri(pictureName)) }
            };

            Dictionary.Add(TileView, this);
        }

        //private Image getTileImage(int row, int col)
        //{
        //    //TODO get image from our server
        //    return new Image
        //    {
        //        Source = ImageSource.FromUri(new Uri("Bitmap" + row + col + ".png"))
        //    };
        //}
    }
}
