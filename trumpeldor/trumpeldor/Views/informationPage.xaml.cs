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
        bool isGeneral;
		public informationPage ()
		{
			InitializeComponent ();
            gc = GameController.getInstance();
            generalInformation.Text = gc.GetGeneralInformation();
            isGeneral = true;
            SetScrollViews(gc.GetMainImages(), gc.GetMainVideos());
        }

        public informationPage(Attraction attraction) : this()
        {
            generalInformation.Text = attraction.description;
            isGeneral = false;
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

        private void ShowMessagesInStart()
        {
            Task.Run(() =>
            {
                List<OpenMessage> messagesToShow = gc.GetOpenMessages();
                foreach (OpenMessage om in messagesToShow)
                {
                    Device.BeginInvokeOnMainThread(async () => {
                        await DisplayAlert(om.title, om.data, AppResources.ok);
                    });
                }
            });
        }

        protected override void OnAppearing()
        {
            base.OnAppearing();
            if(isGeneral)
                ShowMessagesInStart();
        }
    }
}