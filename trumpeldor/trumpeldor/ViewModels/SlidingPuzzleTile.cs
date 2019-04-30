using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using Xamarin.Forms;

namespace trumpeldor.ViewModels
{
	public class SlidingPuzzleTile 
	{
        //const string UrlPrefix = "http://xamarin.github.io/xamarin-forms-book-samples/XamagonXuzzle/";
        //string urlPrefix = "http://" + ServerConection.IP + ":" + ServerConection.PORT + "/media/";

        public static Dictionary<View, SlidingPuzzleTile> Dictionary { get; } = new Dictionary<View, SlidingPuzzleTile>();

        public int currentRow { set; get; }

        private int correctRow;

        public int currentCol { set; get; }

        private int correctCol;

        public View TileView { private set; get; }

        public SlidingPuzzleTile(int row, int col, string pictureName)
        {
            currentRow = row;
            correctRow = row;
            currentCol = col;
            correctCol = col;

            TileView = new ContentView
            {
                Padding = new Thickness(1),
                //Content = getTileImage(row, col)
                Content = new Image { Source = ImageSource.FromUri(new Uri(pictureName)) }
            };

            Dictionary.Add(TileView, this);
        }

        //private Image getTileImage(int row,int col)
        //{
        //    //TODO get image from our server
        //    return new Image
        //    {
        //        Source = ImageSource.FromUri(new Uri(urlPrefix + "example" + row + col + ".jpg"))
        //    };
        //}

        public bool isTilePossitionIsCorrect()
        {
            return correctCol == currentCol && correctRow == currentRow;
        }
        
	}
}