using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

using Android.App;
using Android.Content;
using Android.OS;
using Android.Runtime;
using Android.Views;
using Android.Widget;
using trumpeldor;
using Java.IO;
using Xamarin.Forms.Platform.Android;
using Xamarin.Forms;
using Plugin.CurrentActivity;
using Android.Graphics;
using Android.Support.V4.Content;
using System.Threading.Tasks;
using Android.Provider;

namespace trumpeldor.Droid
{
    class ShareImplementation : IShare
    {
        public Task ShareOnSocialMedia(string imageName)
        {
            Intent shareIntent = new Intent();
            shareIntent.SetAction(Intent.ActionSend);
            shareIntent.PutExtra(Intent.ExtraText, "Trumpeldor Application");
            shareIntent.SetType("image/*");
            var path = Android.OS.Environment.GetExternalStoragePublicDirectory(Android.OS.Environment.DirectoryPictures).AbsolutePath;
            //string absPath = path + "/trumpeldor/photo1.jpg";
            string absPath = path + "/trumpeldor/" + imageName;
            shareIntent.PutExtra(Intent.ExtraStream, Android.Net.Uri.Parse("file://" + absPath));
            MainActivity.Instance.StartActivity(Intent.CreateChooser(shareIntent, "Share via"));
            return Task.FromResult(0);
        }

        public void ShareOnSocialMedia(string message, ImageSource image)
        {
            throw new NotImplementedException();
        }
    }
}