﻿using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace trumpeldor.Views
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class AccessFacebookProfile : ContentPage
    {

        private string ClientId = "722384804784862";

        public AccessFacebookProfile()
        {
            try
            {
                InitializeComponent();

            
                var apiRequest =
                    "https://www.facebook.com/dialog/oauth?client_id="
                    + ClientId
                    + "&display=popup&state={st=state123abc,ds=123456789}&response_type=token&redirect_uri=https://www.facebook.com/connect/login_success.html";

            
              /*  var webView = new WebView
                {
                    Source = "http://xamarin.com"
                    //Source = apiRequest,
                    //HeightRequest = 1
                };*/
                
            webView.Source = apiRequest;



            webView.Navigated += WebViewOnNavigated;

            


                // Content = webView;
            }
             catch (Exception e)
             {
                 Console.WriteLine("ERROR: " + e.Message);
             }

        }
        
        async void WebViewOnNavigated(object sender, WebNavigatedEventArgs e)
        {
            try
            {
                var accessToken = ExtractAccessTokenFromUrl(e.Url);
                if (accessToken != "")
                {
                    await GetFacebookProfileAsync(accessToken);
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("ERROR: " + ex.Message);
            }
        }

        string ExtractAccessTokenFromUrl(string url)
        {

            if (url.Contains("access_token") && url.Contains("&expires_in="))
            {
                //var at = url.Replace("https://www.facebook.com/connect/login_success.html#access_token=", "");
                var at = url.Substring(url.IndexOf("access_token") + 13);
                //var at = url.Replace("https://www.facebook.com/connect/login_success.html#access_token=", "");

                if (Device.RuntimePlatform == "WinPhone" || Device.RuntimePlatform == "Windows")
                {
                    at = url.Substring(url.IndexOf("access_token") + 13);
                }

               // var accessToken = at.Remove(at.IndexOf("&expires_in="));



                return at;
            }

            return string.Empty;
        }

        async Task GetFacebookProfileAsync(string accessToken)
        {
            try
            {
                var requestUrl =
                    "https://graph.facebook.com/v3.2/me/"
                    + "?fields=name,id"
                    + "&access_token=" + accessToken;

                var httpClient = new HttpClient();

                var userJson = await httpClient.GetStringAsync(requestUrl);
                JObject json = JObject.Parse(userJson);
                string username = (string)json["name"];
                string id = (string)json["id"];
                //((App)(Application.Current)).getGameController().SignUp(id, "facebook");
                Application.Current.MainPage = new groupCreationPage();

               // Content= groupCreationPage.xaml;


            }
            catch (Exception e)
            {
                Console.WriteLine("ERROR: " + e.Message);
            }
        }
        
    }
    
}

   
