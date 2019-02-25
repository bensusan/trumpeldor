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
        private GameController gc = ((App)(Application.Current)).getGameController();
        //private GameController.PathLength selectedPathLength;
        private int selectedPathLength;
        public groupCreationPage()
        {
            InitializeComponent();
        }

        public async Task<ContentPage> ShowPastDetailsAsync()
        {
            if (gc.IsUserConnectedRecently())
            {
                bool dialogAnswer = DisplayAlert(AppResources.Hey+", " + gc.currentUser.name + "!", AppResources.Do_you_want_to_continue_last_trip, AppResources.Yes, AppResources.No).Result;
                if (dialogAnswer) {
                    await gc.ContinuePreviousTrip();
                    return new NavigationPage();
                }    
            }
            KeyValuePair<string, List<int>> ans = await gc.LoadRelevantInformationFromLastTrip();
            //ans is in the form of <groupName, playerAges>
            groupNameEntry.Text = ans.Key;
            if (ans.Value != null)
            {
                for (int i = 0; i < ans.Value.Count; i++)
                    AddRowToPlayersGrid(ans.Value[i].ToString());
            }
            return this;            
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
            int nextRow = agesGrid.RowDefinitions.Count;
            agesGrid.RowDefinitions.Add(new RowDefinition { Height = GridLength.Star });
            Label lbl = new Label { Text = nextRow + ")" };
            lbl.SetDynamicResource(VisualElement.StyleProperty, "lableStyle");
            agesGrid.Children.Add(lbl, 0, nextRow);
            Entry entry = new Entry { Keyboard = Keyboard.Numeric };
            if (playerAge != null)
                entry.Text = playerAge;
            entry.SetDynamicResource(VisualElement.StyleProperty, "entryStyle");
            agesGrid.Children.Add(entry, 1, nextRow);
        }


        private void Add_Player_Button_Clicked(object sender, EventArgs e)
        {
            AddRowToPlayersGrid(null);
        }

        private async void Start_Trip_Button_Clicked(object sender, EventArgs e)
        {
            String groupName = groupNameEntry.Text;
            List<int> agesList = new List<int>();
            foreach(View child in agesGrid.Children)
            {
                if(child is Entry)
                {
                    agesList.Add(Int32.Parse(((Entry)child).Text));
                }
            }
            var existingPages = Navigation.NavigationStack.ToList();
            foreach (var page in existingPages)
            {
                Navigation.RemovePage(page);
            }
            await gc.CreateTrip(groupName, agesList, selectedPathLength);
            await DisplayAlert("", AppResources.group_name +" " + gc.currentTrip.groupName + " " + AppResources.Players_Ages + gc.currentTrip.playersAges[0].ToString() + " "+ AppResources.First_Attraction + gc.currentTrip.GetCurrentAttraction().ToString(), AppResources.ok);
            Application.Current.MainPage = new NavigationPage();
        }
    }
}