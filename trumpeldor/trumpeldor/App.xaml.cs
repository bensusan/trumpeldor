using System;
using System.Collections.Generic;
using trumpeldor.Views;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

[assembly: XamlCompilation(XamlCompilationOptions.Compile)]
namespace trumpeldor
{
    public partial class App : Application
    {
        
        private GameController gameController;//here we wirte global vars

        static Xamarin.Forms.NavigationPage _NavPage;

        public App()
        {
            InitializeComponent();
            gameController = GameController.getInstance();
            //MainPage = new Views.FirstPage();
            Xamarin.Forms.NavigationPage.SetHasNavigationBar(this, false);
            MainPage = new Xamarin.Forms.NavigationPage(new FirstPage());
            

            //MainPage = new Xamarin.Forms.NavigationPage(new FirstPage());
        }

        protected override void OnStart()
        {
            // Handle when your app starts
        }

        protected override void OnSleep()
        {
            // Handle when your app sleeps
        }

        protected override void OnResume()
        {
            // Handle when your app resumes
        }

        public GameController getGameController()
        {
            return gameController;
        }

        
    }
}
