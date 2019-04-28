using Plugin.Media.Abstractions;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace trumpeldor.Views
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class ShowSavedImagesPage : ContentPage
    {
        Image img1 = null;
        List<string> photos = null;
        public ShowSavedImagesPage()
        {
            InitializeComponent();
            photos = new List<string>();
            Button shareButton = new Button
            {
                Text = "Share",
                VerticalOptions = LayoutOptions.CenterAndExpand,
                HorizontalOptions = LayoutOptions.CenterAndExpand
            };
            ImgLayout.Children.Add(shareButton);
            Button pickPictureButton = new Button
            {
                Text = "Pick Photo",
                VerticalOptions = LayoutOptions.CenterAndExpand,
                HorizontalOptions = LayoutOptions.CenterAndExpand
            };
            ImgLayout.Children.Add(pickPictureButton);
            pickPictureButton.Clicked += async (sender, e) =>
            {
                pickPictureButton.IsEnabled = false;
                Stream stream = await DependencyService.Get<IPicturePicker>().GetImageStreamAsync();
                
                if (stream != null)
                {
                    Image image = new Image
                    {
                        Source = ImageSource.FromStream(() => stream),
                        BackgroundColor = Color.Gray
                    };
                    ImgLayout.Children.Add(image);
                    ImageSource s = image.Source;
                    string str = s.ToString();
                    
                    photos.Add(image.Source.ToString());
                    if(img1==null)
                    {
                        img1 = image;
                        //ImageSource isrc= img1.Source;
                    }

                }

                pickPictureButton.IsEnabled = true;
            };
            shareButton.Clicked += async (sender, e) =>
            {
                // string str="";
               // await DependencyService.Get<IShare>().ShareOnSocialMedia(str);

            };

        }

    }
}