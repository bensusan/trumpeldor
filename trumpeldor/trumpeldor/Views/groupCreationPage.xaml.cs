using Newtonsoft.Json.Linq;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using trumpeldor.Models;
using trumpeldor.SheredClasses;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace trumpeldor.Views
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class groupCreationPage : ContentPage
    {
        private GameController gc;
        private static int DELETE_PLAYER_COLUMN = 0, PLAYER_NUMBER_COLUMN = 1, PLAYER_AGE_COLUMN = 2;
        public groupCreationPage() : this("", User.SOCIAL_NETWORK.Anonymous){}

        public groupCreationPage(string userName, User.SOCIAL_NETWORK socialNetwork){
            InitializeComponent();
            InitPicker();
            addButton.Source = ServerConection.URL_MEDIA + "plus.png";
            removeButton.Source = ServerConection.URL_MEDIA + "delete.png";
            gc = GameController.getInstance();
            string socialnetworkString;
            User.SocialNetwork2string.TryGetValue(socialNetwork, out socialnetworkString);
            gc.SignUp(userName, socialnetworkString);
        }

        private void InitPicker()
        {
            picker.Items.Add(AppResources.short_path);
            picker.Items.Add(AppResources.medium_path);
            picker.Items.Add(AppResources.long_path);
        }

        protected override async void OnAppearing()
        {
            base.OnAppearing();
            if(!await ShowPastDetails())
                Application.Current.MainPage = new NavigationPage();

        }

        public async Task<bool> ShowPastDetails()
        {
            if (!gc.IsNewUser()){
                if (gc.IsUserConnectedRecently()){
                    int dialogAns = 0;
                    
                    bool dialogAnswer = await DisplayAlert(
                    AppResources.Hey + ", " + gc.currentUser.name + "!",
                    AppResources.Do_you_want_to_continue_last_trip,
                    AppResources.Yes,
                    AppResources.No);

                    if (dialogAnswer)
                        dialogAns = 1;
                    else
                        dialogAns = 2;
                    
                    if (dialogAns == 1){
                        gc.ContinuePreviousTrip();
                        //Application.Current.MainPage = new NavigationPage();
                        return false;

                    }
                }
                RelevantInformation ans = gc.LoadRelevantInformationFromLastTrip();
                groupNameEntry.Text = ans.groupName;
                if (ans.playersAges != null)
                    for (int i = 0; i < ans.playersAges.Count; i++)
                        AddRowToPlayersGrid(ans.playersAges[i].ToString());
            }
            return true;
        }
        
        private void AddRowToPlayersGrid(String playerAge)
        {
            if (playerAge != null)
                ((Entry)agesGrid.Children.ElementAt(agesGrid.Children.Count - 1)).Text = playerAge;
            int nextRow = agesGrid.Children.Select(c => Grid.GetRow(c)).Max()+1;//agesGrid.RowDefinitions.Count;
            agesGrid.RowDefinitions.Add(new RowDefinition { Height = GridLength.Star });

            //Delete imageButton addition
            ImageButton removeButton = new ImageButton { Source = ServerConection.URL_MEDIA + "delete.png" };
            removeButton.Clicked += removeRow_Clicked;
            removeButton.SetDynamicResource(VisualElement.StyleProperty, "regularCircleImageButtonStyle");
            agesGrid.Children.Add(removeButton, DELETE_PLAYER_COLUMN, nextRow);

            //Player number addition
            Label lbl = new Label { Text = nextRow + ")" };
            lbl.SetDynamicResource(VisualElement.StyleProperty, "labelStyle");
            agesGrid.Children.Add(lbl, PLAYER_NUMBER_COLUMN, nextRow);

            //Player's age addition
            Entry entry = new Entry { Keyboard = Keyboard.Numeric };            
            entry.SetDynamicResource(VisualElement.StyleProperty, "entryStyle");
            agesGrid.Children.Add(entry, PLAYER_AGE_COLUMN, nextRow);
        }


        private void Add_Player_Button_Clicked(object sender, EventArgs e)
        {
            AddRowToPlayersGrid(null);
        }

        private void Start_Trip_Button_Clicked(object sender, EventArgs e)
        {
            String groupName = groupNameEntry.Text;
            List<int> agesList = new List<int>();
            foreach (View child in agesGrid.Children){
                if (child is Entry){
                    string age = ((Entry)child).Text;
                    if (age != "" && age != null)
                        agesList.Add(Int32.Parse(age));
                }
            }
            if (groupName != "" && agesList.Count != 0 && picker.SelectedIndex != -1){
                gc.CreateTrip(groupName, agesList, picker.SelectedIndex + 1);
                var existingPages = Navigation.NavigationStack.ToList();
                foreach (var page in existingPages)
                    Navigation.RemovePage(page);
                Application.Current.MainPage = new NavigationPage();
            }
            else
                DisplayAlert(AppResources.error, AppResources.error_in_group_creation, AppResources.ok);
        }

        private void removeRow_Clicked(object sender, EventArgs e)
        {
            int row = Grid.GetRow((ImageButton)sender);
            foreach (var child in agesGrid.Children.ToList().Where(child => Grid.GetRow(child) == row))
                agesGrid.Children.Remove(child);
            foreach (var child in agesGrid.Children.ToList().Where(child => Grid.GetRow(child) > row)){
                Grid.SetRow(child, Grid.GetRow(child) - 1);
                if(child is Label)
                    ((Label)child).Text = Grid.GetRow(child) + ")";
            }
            agesGrid.RowDefinitions.RemoveAt(agesGrid.RowDefinitions.Count - 1);
        }
    }
}