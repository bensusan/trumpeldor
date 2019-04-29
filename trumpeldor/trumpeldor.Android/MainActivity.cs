using System;

using Android.App;
using Android.Content.PM;
using Android.Runtime;
using Android.Views;
using Android.Widget;
using Android.OS;
using trumpeldor.Configuration;
using trumpeldor.Droid.Configuration;
using Plugin.CurrentActivity;
using System.IO;
using System.Threading.Tasks;
using Android.Content;
using Xamarin.Forms;
using trumpeldor;

using trumpeldor.Services;
using Android.Gms.Auth.Api.SignIn;
using Android.Gms.Auth.Api;
using Xamarin.Forms;
using trumpeldor.Services.Contracts;

namespace trumpeldor.Droid
{
    [Activity(Label = "trumpeldor", Icon = "@mipmap/icon", Theme = "@style/MainTheme", MainLauncher = true, ConfigurationChanges = ConfigChanges.ScreenSize | ConfigChanges.Orientation)]
    public class MainActivity : global::Xamarin.Forms.Platform.Android.FormsAppCompatActivity
        //, IGoogleAuthenticationDelegate
    {
        // Field, property, and method for Picture Picker
        public static readonly int PickImageId = 1000;
        internal static MainActivity Instance { get; private set; }
        PhotosController pc = PhotosController.GetInstance();
        public TaskCompletionSource<Stream> PickImageTaskCompletionSource { set; get; }

        protected override void OnCreate(Bundle savedInstanceState)
        {
            TabLayoutResource = Resource.Layout.Tabbar;
            ToolbarResource = Resource.Layout.Toolbar;

            base.OnCreate(savedInstanceState);

            DependencyService.Register<IGoogleManager, GoogleManager>();

            Instance = this;
            CrossCurrentActivity.Current.Init(this, savedInstanceState);
            global::Xamarin.Forms.Forms.Init(this, savedInstanceState);
            ConfigurationManager.Initialize(new AndroidConfigurationStreamProviderFactory(() => this));
            Xamarin.FormsMaps.Init(this, savedInstanceState);//for maps init
            DependencyService.Register<IShare, ShareImplementation>();
            LoadApplication(new App());
        }

        public override void OnRequestPermissionsResult(int requestCode, string[] permissions, Android.Content.PM.Permission[] grantResults)
        {
            Plugin.Permissions.PermissionsImplementation.Current.OnRequestPermissionsResult(requestCode, permissions, grantResults);
            base.OnRequestPermissionsResult(requestCode, permissions, grantResults);
        }
        

        protected override void OnActivityResult(int requestCode, Result resultCode, Intent intent)
        {
            base.OnActivityResult(requestCode, resultCode, intent);
            if (requestCode == 1)
            {
                GoogleSignInResult result = Auth.GoogleSignInApi.GetSignInResultFromIntent(intent);
                GoogleManager.Instance.OnAuthCompleted(result);
			}

            else if (requestCode == PickImageId)
            {
                if ((resultCode == Result.Ok) && (intent != null))
                {
                    Android.Net.Uri uri = intent.Data;
                    Stream stream = ContentResolver.OpenInputStream(uri);

                    // Set the Stream as the completion of the Task
                    PickImageTaskCompletionSource.SetResult(stream);
                }
                else
                {
                    PickImageTaskCompletionSource.SetResult(null);
                }
            }
        }
    }
}