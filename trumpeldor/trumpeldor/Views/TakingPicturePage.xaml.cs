﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Plugin;
using Plugin.Media;
using Plugin.Media.Abstractions;
using Rg.Plugins.Popup.Services;
using trumpeldor;
using trumpeldor.SheredClasses;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace trumpeldor.Views
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class TakingPicturePage : ContentPage
	{
        private int timesPressed = 0;
        PhotosController pc;
        private System.IO.Stream source=null;
        private MediaFile photo;
        private static int count = 1;
        string aPpath;
        string path;
        ImageSource imgSrc;
        private GameController gc;
        private TakingPicture tp;
        private Attraction attraction;

        public TakingPicturePage (TakingPicture tp, Attraction attraction)
		{
			InitializeComponent ();
            pc = PhotosController.GetInstance();
            gc = GameController.getInstance();
            scoreLabel.Text = AppResources.score + ": " + gc.GetScore();
            CameraButton.Clicked += CameraButton_Clicked;
            subtitles.Source = ServerConection.URL_MEDIA + "subtitles.jpg";
            info.Source = ServerConection.URL_MEDIA + "info.jpg";
            playVideo.Source = ServerConection.URL_MEDIA + "playVideo.jpg";
            how.Source = ServerConection.URL_MEDIA + "how.png";
            this.tp = tp;
            this.attraction = attraction;
        }

        private async void CameraButton_Clicked(object sender, EventArgs e)
        {
            Button clicked = (Button)sender;//disable button
            clicked.IsEnabled = false;

            if (timesPressed == 0)//take photo
            {

                timesPressed++;
                photo = null;
                photo = await Plugin.Media.CrossMedia.Current.TakePhotoAsync(new Plugin.Media.Abstractions.StoreCameraMediaOptions()
                {
                    SaveToAlbum = true,
                    Directory = "BGUART",
                    Name = "photo" + count.ToString()
                });
                count++;
                //save btn
                

                if (photo != null)
                {
                    source = photo.GetStream();
                    PhotoImage.Source = ImageSource.FromStream(() => { return source; });

                    imgSrc = PhotoImage.Source;

                    //Get the public album path
                    aPpath = photo.AlbumPath;

                    //Get private path
                    path = photo.Path;
                }

                CameraButton.Text = AppResources.save_and_continue;
                CameraButton.BackgroundColor = Color.White;
                AddToLayout(BtnLayout,AppResources.share, ShareButton_Clicked, Color.Orange);


                clicked.IsEnabled = true;//enable button
            }

            else if (timesPressed == 1)//save btn
            {
                if (source != null)
                {

                    pc.AddToPhotosSourcesList(aPpath);
                    pc.AddToPhotosSourcesList(path);

                    //back to previous page
                    scoreLabel.Text = AppResources.score + ": " + gc.EditScore(ScoreRule.Kinds.Taking_Picture_Done);
                    gc.FinishAttraction();
                    await Navigation.PopModalAsync();

                }

                    //AddToLayout(BtnLayout, "Save and Continue", SaveBtn_Clicked);//save and continue           
            }  
        
        }

        private async void ShareButton_Clicked(object sender, EventArgs e)
        {
            int index = aPpath.IndexOf("photo");
            string imgName = aPpath.Substring(index, aPpath.Length - index );
            if (Device.RuntimePlatform == Device.iOS)
            {
                DependencyService.Get<IShare>().ShareOnSocialMedia("BGUART", imgSrc);
            }
            else if (Device.RuntimePlatform == Device.Android)
            {
                await DependencyService.Get<IShare>().ShareOnSocialMedia(imgName);
            }
            
        }

        private void AddToLayout(StackLayout layout, string btnName, EventHandler e, Color c)
        {
            Button btn = new Button();
            btn.Text = btnName;
            btn.Clicked += e;
            btn.BackgroundColor = c;
            btn.Style = (Style)Application.Current.Resources["largeButtonStyle"];
            layout.Children.Add(btn);
        }

        private void EnableButtons(bool toEnable)
        {
            foreach (Button btn in BtnLayout.Children)
            {
                btn.IsEnabled = toEnable;
            }
        }

        private async void HowToPlay_Button_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new instructionsPage(tp));
        }

        private async void PlayVideo_Clicked(object sender, EventArgs e)
        {
            if (attraction.videosURLS.Count > 0)
                await Navigation.PushModalAsync(new ShowVideoAndTextPage(attraction.videosURLS[0], true));
        }

        private async void Subtitles_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new ShowVideoAndTextPage("", false));
        }

        private void Information_Button_Clicked(object sender, EventArgs e)
        {

        }
    }
}
