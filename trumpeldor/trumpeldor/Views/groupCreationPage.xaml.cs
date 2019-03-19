using Newtonsoft.Json.Linq;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using trumpeldor.SheredClasses;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace trumpeldor.Views
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class groupCreationPage : ContentPage
    {
        private GameController gc;
        //private GameController.PathLength selectedPathLength;
        private int selectedPathLength;

        public groupCreationPage() : this("", User.SOCIAL_NETWORK.Anonymous){}

        public groupCreationPage(string userName, User.SOCIAL_NETWORK socialNetwork){
            InitializeComponent();
            gc = GameController.getInstance();
            string socialnetworkString;
            User.SocialNetwork2string.TryGetValue(socialNetwork, out socialnetworkString);
            gc.SignUp(userName, socialnetworkString);
        }

        protected override async void OnAppearing()
        {
            base.OnAppearing();
            await ShowPastDetails();
        }

        public async Task ShowPastDetails()
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
                    
                    
                    if (dialogAns == 1)
                    {
                        gc.ContinuePreviousTrip();
                        Application.Current.MainPage = new NavigationPage();
                        return;
                    }

                }
                RelevantInformation ans = gc.LoadRelevantInformationFromLastTrip();
                groupNameEntry.Text = ans.groupName;
                if (ans.playersAges != null)
                    for (int i = 0; i < ans.playersAges.Count; i++)
                        AddRowToPlayersGrid(ans.playersAges[i].ToString());
            }
        }

        private void Select_Short_Path_Button_Clicked(object sender, EventArgs e)
        {
            Select_Path_Button_Clicked(sender, e);
            //selectedPathLength = GameController.PathLength.shortPath;
            selectedPathLength = 1;
        }
        private void Select_Medium_Path_Button_Clicked(object sender, EventArgs e)
        {
            Select_Path_Button_Clicked(sender, e);
            //selectedPathLength = GameController.PathLength.mediumPath;
            selectedPathLength = 2;
        }
        private void Select_Long_Path_Button_Clicked(object sender, EventArgs e)
        {
            Select_Path_Button_Clicked(sender, e);
            //selectedPathLength = GameController.PathLength.longPath;
            selectedPathLength = 3;
        }

        private void Select_Path_Button_Clicked(object sender, EventArgs e)
        {
            StartTripButton.IsEnabled = true;
            int count = lengthButtonGroup.Children.Count;
            View v = null;
            for (int i = 0; i < count; i++)
            {
                v = lengthButtonGroup.Children.ElementAt(i);
                v.IsEnabled = true;
            }
            ((Button)sender).IsEnabled = false;
        }
        
        private void AddRowToPlayersGrid(String playerAge)
        {
            if (playerAge != null)
                ((Entry)agesGrid.Children.ElementAt(agesGrid.Children.Count - 1)).Text = playerAge;
            int nextRow = agesGrid.RowDefinitions.Count;
            agesGrid.RowDefinitions.Add(new RowDefinition { Height = GridLength.Star });
            Label lbl = new Label { Text = nextRow + ")" };
            lbl.SetDynamicResource(VisualElement.StyleProperty, "lableStyle");
            agesGrid.Children.Add(lbl, 0, nextRow);
            Entry entry = new Entry { Keyboard = Keyboard.Numeric };            
            entry.SetDynamicResource(VisualElement.StyleProperty, "entryStyle");
            agesGrid.Children.Add(entry, 1, nextRow);
        }


        private void Add_Player_Button_Clicked(object sender, EventArgs e)
        {
            AddRowToPlayersGrid(null);
        }

        private void Start_Trip_Button_Clicked(object sender, EventArgs e)
        {
            String groupName = groupNameEntry.Text;
            List<int> agesList = new List<int>();
            try
            {
                foreach (View child in agesGrid.Children)
                {
                    if (child is Entry)
                    {
                        string age = ((Entry)child).Text;
                        if (age != "" && age != null)
                            agesList.Add(Int32.Parse(age));
                    }
                }

                var existingPages = Navigation.NavigationStack.ToList();
                foreach (var page in existingPages)
                {
                    Navigation.RemovePage(page);
                }
                if (groupName != "" && agesList.Count != 0 &&
                    (selectedPathLength == 1 || selectedPathLength == 2 || selectedPathLength == 3))
                {
                    gc.CreateTrip(groupName, agesList, selectedPathLength);
                    Application.Current.MainPage = new NavigationPage();
                }
                else
                {
                    DisplayAlert("Illegal Input!", "You must fill all the fields", "OK");

                }
            }
            catch (Exception ex)
            {
                if (!(groupName != null && agesList.Count != 0 &&
                    (selectedPathLength == 1 || selectedPathLength == 2 || selectedPathLength == 3)))
                        DisplayAlert("Illegal Input!", "You must fill all the fields", "OK");

            }
        }
    }
}