using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;
using trumpeldor.Models;
using trumpeldor.Services.Contracts;
using trumpeldor.SheredClasses;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace trumpeldor.Views
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class AccessGoogleProfile : ContentPage
    {
        private readonly IGoogleManager _googleManager;
        //private readonly IPageDialogService _dialogService;

        //public DelegateCommand GoogleLoginCommand { get; set; }
        //public DelegateCommand GoogleLogoutCommand { get; set; }

        //private string _title;
        //public string Title
        //{
        //    get { return _title; }
        //    set { SetProperty(ref _title, value); }
        //}

        //private bool _isLogedIn;

        //public bool IsLogedIn
        //{
        //    get { return _isLogedIn; }
        //    set { SetProperty(ref _isLogedIn, value); }
        //}

        private GoogleUser _googleUser;

        //public GoogleUser GoogleUser
        //{
        //    get { return _googleUser; }
        //    set { SetProperty(ref _googleUser, value); }
        //}

        //public MainPageViewModel(IGoogleManager googleManager/*, IPageDialogService dialogService*/)
        //{
            //_googleManager = googleManager;
            ////_dialogService = dialogService;

            ////IsLogedIn = false;
            ////GoogleLoginCommand = new DelegateCommand(GoogleLogin);
            ////GoogleLogoutCommand = new DelegateCommand(GoogleLogout);
        //}

        //private void GoogleLogout()
        //{
        //    _googleManager.Logout();
        //    IsLogedIn = false;
        //}

        private void GoogleLogin()
        {
            _googleManager.Login(OnLoginComplete);
        }

        private void OnLoginComplete(GoogleUser googleUser, string message)
        {
            Device.BeginInvokeOnMainThread(async () =>
            {
                await DisplayAlert("Login complete", googleUser + " " + message, AppResources.ok);
            });
            if (googleUser != null)
            {
                _googleUser = googleUser;
                Device.BeginInvokeOnMainThread(async () => {
                    await DisplayAlert(googleUser.ID, googleUser.Name, AppResources.ok);
                });
                Application.Current.MainPage = new groupCreationPage(googleUser.ID, User.SOCIAL_NETWORK.Google);
                //IsLogedIn = true;
            }
            else
            {
                //_dialogService.DisplayAlertAsync("Error", message, "Ok");
            }
        }

        //public void OnNavigatedFrom(NavigationParameters parameters)
        //{

        //}

        //public void OnNavigatingTo(NavigationParameters parameters)
        //{

        //}

        //public void OnNavigatedTo(NavigationParameters parameters)
        //{
        //    if (parameters.ContainsKey("title"))
        //        Title = (string)parameters["title"] + " and Prism";
        //}

        public AccessGoogleProfile ()
		{
			InitializeComponent ();
            _googleManager = DependencyService.Get<IGoogleManager>();
        }

        protected override void OnAppearing()
        {
            base.OnAppearing();
            GoogleLogin();
        }
    }
      
}