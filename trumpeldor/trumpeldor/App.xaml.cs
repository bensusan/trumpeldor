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
        
        private GameController gameController;

        public App()
        {
            InitializeComponent();
            gameController = new GameController();
            MainPage = new Views.FirstPage();
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
