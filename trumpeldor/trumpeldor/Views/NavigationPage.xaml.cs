using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;
using trumpeldor.SheredClasses;
using trumpeldor;
namespace trumpeldor.Views
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class NavigationPage : ContentPage
	{
        //        gc.currentTrip.GetCurrentAttraction();//-for the hint
        public Attraction nextAttraction;
        public static int hintsIndex = 0;
        trumpeldor.SheredClasses.Point p;
        public GameController gc = ((App)Application.Current).getGameController();
        public NavigationPage ()
		{
			InitializeComponent ();
            //-------------------------------------------------------
            nextAttraction = gc.currentTrip.GetCurrentAttraction();
            //-------------------------------------------------------

            //-------------------------------------------------------
            /*
            nextAttraction = new Attraction();
            List<Hint> hintsLst = new List<Hint>();
            Hint h1 = new Hint();
            h1.id = 0; h1.kind = "HT"; h1.data = "first text";
            Hint h2 = new Hint();
            h2.id = 1; h2.kind = "HP"; h2.data = "x.jpg";
            Hint h3 = new Hint();
            h3.id = 2; h3.kind = "HT"; h3.data = "second text";
            Hint h4 = new Hint();
            h4.id = 3; h4.kind = "HP"; h4.data = "y.jpg";
            hintsLst.Add(h1); hintsLst.Add(h2); hintsLst.Add(h3); hintsLst.Add(h4);
            nextAttraction.hints = hintsLst;
            nextAttraction.x = 31; nextAttraction.x = 34;
            */
            //-------------------------------------------------------

            p = new trumpeldor.SheredClasses.Point(nextAttraction.x, nextAttraction.y);
            scoreLabel.Text = AppResources.score+ ": " + gc.currentTrip.score;
            //mapImage.Source = ImageSource.FromResource("trumpeldor.Resources.MapIcon.png");
            mapImage.Text = AppResources.map;
            //SheredClasses.Clue nextClue = gc.GetFisrtHint();
            //nextClue.addToLayout(hintsLayout);
        }

        private async void Get_Hint_Button_Clicked(object sender, EventArgs e)
        {
            if (nextAttraction != null && hintsIndex>=0 && hintsIndex<nextAttraction.hints.Count)
            {
                
                Hint nextHint;
                nextHint = nextAttraction.hints[hintsIndex];
                if (nextHint != null)
                {
                    if (nextHint.kind.Equals("HM"))//hint map
                    {
                        await Navigation.PushModalAsync(new MapPage(p));
                        Button hintBtn = (Button)FindByName("hintBtn");
                        if (hintBtn != null)
                            hintBtn.IsEnabled = false;
                    }
                    else
                    {
                        await Navigation.PushModalAsync(new HintPage(nextHint));
                        if (hintsIndex == nextAttraction.hints.Count - 2)
                        {
                            Button hintBtn = (Button)FindByName("hintBtn");
                            if(hintBtn != null)
                                hintBtn.Text = "Last Hint";
                        }
                    }
                    //nextHint.addToLayout(hintsLayout);
                    //scoreLabel.Text = "score: " + gc.currentTrip.score;
                    addToLayout(hintsLayout);


                    hintsIndex++;
                }
            }
            
        }

        private void Next_Destination_Button_Clicked(object sender, EventArgs e)
        {
            DisplayAlert(AppResources.success, AppResources.You_have_Reached_Your_Destionation, AppResources.ok);
            var existingPages = Navigation.NavigationStack.ToList();
            foreach (var page in existingPages)
            {
                Navigation.RemovePage(page);
            }
            Application.Current.MainPage = new AttractionPage();
        }

        private async void mapImage_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new MapPage());
        }

        private async void DynamicBtn_Clicked(object sender, EventArgs e)
        {
            try
            {
                Button clicked = (Button)sender;
                string strIdx = clicked.Text.Substring(5, clicked.Text.Length - 5);
                int currIdx = Int32.Parse(strIdx) -1;
                Hint toShow = nextAttraction.hints[currIdx];
                if (toShow.kind.Equals("HM"))//hint map
                {
                    await Navigation.PushModalAsync(new MapPage(p));
                }
                else
                {
                    await Navigation.PushModalAsync(new HintPage(toShow));
                }
            }

            catch (Exception exp)
            {
                Console.WriteLine(exp.Message);
            }
            
        }
        

        private void addToLayout(StackLayout layout)
        {
            Button btn = new Button();
            string strIndex = (hintsIndex + 1).ToString();
            btn.Text = "Hint " + strIndex;
            btn.AutomationId = "savedHint" + strIndex;
            btn.Clicked += DynamicBtn_Clicked;
            layout.Children.Add(btn);
        }
    }
}