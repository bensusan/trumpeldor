using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;
using trumpeldor.SheredClasses;

namespace trumpeldor.Views
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class informationPage : ContentPage
	{
        GameController gc;
		public informationPage ()
		{
			InitializeComponent ();
            gc = GameController.getInstance();
            generalInformation.Text = gc.GetGeneralInformation();
            SetScrollViews(gc.GetMainImages(), gc.GetMainVideos());
        }

        public informationPage(Attraction attraction) : this()
        {
            generalInformation.Text = attraction.description;
            SetScrollViews(attraction.picturesURLS, attraction.videosURLS);
        }

        public void SetScrollViews(List<string> imagesNames, List<string> videosNames)
        {
            foreach (string pictureURL in imagesNames)
            {
                stackGalleryImages.Children.Add(new Image
                {
                    Source = gc.GetMediaURLFromName(pictureURL),
                    HeightRequest = gc.GetHeightSizeOfPage() / 3,
                    WidthRequest = gc.GetWidthSizeOfPage()*3/4
                });
            }
            foreach (string videoURL in videosNames)
            {
                stackGalleryVideos.Children.Add(new WebView
                {
                    Source = gc.GetMediaURLFromName(videoURL),
                    HeightRequest = gc.GetHeightSizeOfPage()/3,
                    WidthRequest = gc.GetWidthSizeOfPage() * 3 / 4
                });
            }
        }
    }
}