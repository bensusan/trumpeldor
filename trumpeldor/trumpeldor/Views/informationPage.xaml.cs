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
        string generalInfoTextStart = "";

		public informationPage ()
		{
			InitializeComponent ();
            gc = GameController.getInstance();
            generalInfoTextStart = "General information, links, ...";
            generalInformation.FormattedText = new FormattedString();
            generalInformation.FormattedText.Spans.Add(new Span { Text = generalInfoTextStart, Style = (Style)Application.Current.Resources["labelStyle"] });
            isGeneral = true;
            SetScrollViews(gc.GetMainImages(), gc.GetMainVideos());
        }

        public informationPage(Attraction attraction) : this()
        {
            generalInfoTextStart = attraction.description;
            generalInformation.FormattedText = new FormattedString();
            generalInformation.FormattedText.Spans.Add(new Span { Text = generalInfoTextStart, Style = (Style)Application.Current.Resources["labelStyle"] });
            isGeneral = false;
            SetScrollViews(attraction.picturesURLS, attraction.videosURLS);
        }

        public void SetScrollViews(List<string> imagesNames, List<string> videosNames)
        {
            foreach (string pictureURL in imagesNames)
            {
                stackGalleryImages.Children.Add(new Image
                {
                    Source = pictureURL,
                    HeightRequest = gc.GetHeightSizeOfPage() / 3,
                    WidthRequest = gc.GetWidthSizeOfPage()*3/4
                });
            }
            foreach (string videoURL in videosNames)
            {
                stackGalleryVideos.Children.Add(new WebView
                {
                    Source = videoURL,
                    HeightRequest = gc.GetHeightSizeOfPage()/3,
                    WidthRequest = gc.GetWidthSizeOfPage() * 3 / 4
                });
            }
        }

        private void ShowMessagesInStart()
        {
            List<OpenMessage> messagesToShow = gc.GetOpenMessages();
            foreach (OpenMessage om in messagesToShow) {
                generalInformation.FormattedText.Spans.Add(new Span { Text = "\n\n" + om.title + ":", FontSize = 26, TextColor = Color.Black, FontAttributes = FontAttributes.Bold });
                generalInformation.FormattedText.Spans.Add(new Span { Text = "\n" + om.data, FontSize = 20, TextColor = Color.Black });
                //Device.BeginInvokeOnMainThread(async () => {
                //    await DisplayAlert(om.title, om.data, AppResources.ok);
                //});
            }
        }

        protected override void OnAppearing()
        {
            base.OnAppearing();
            if(isGeneral)
                ShowMessagesInStart();
        }
    }
}