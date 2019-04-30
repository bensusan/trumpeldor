using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using trumpeldor.ViewModels;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;
using trumpeldor.SheredClasses;
namespace trumpeldor.Views
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class SlidingPuzzlePage : ContentPage
	{
        private SlidingPuzzleTile[,] tiles;
        private int emptyRow ;
        private int emptyCol ;
        private double tileSize;
        private bool isBusy;
        private SlidingPuzzle sp;
        private GameController gc;

        public SlidingPuzzlePage (SlidingPuzzle sp)
		{
            InitializeComponent ();
            this.gc = GameController.getInstance();
            how.Source = ServerConection.URL_MEDIA + "how.png";
            this.sp = sp;
            tiles = new SlidingPuzzleTile[sp.width, sp.height];
            emptyRow = sp.width - 1;
            emptyCol = sp.height - 1;

            for (int row = 0; row < sp.width; row++)
            {
                for (int col = 0; col < sp.height; col++)
                {
                    if (row == emptyRow && col == emptyCol)
                    {
                        break;
                    }
                    SlidingPuzzleTile tile = new SlidingPuzzleTile(row, col, sp.piecesURLS[row*sp.width +col]);

                    TapGestureRecognizer tapGestureRecognizer = new TapGestureRecognizer();
                    tapGestureRecognizer.Tapped += OnTileTapped;
                    tile.TileView.GestureRecognizers.Add(tapGestureRecognizer);

                    tiles[row, col] = tile;
                    absoluteLayout.Children.Add(tile.TileView);
                }
            }

            shuffle();
        }

        protected override void OnAppearing()
        {
            base.OnAppearing();
            scoreLabel.Text = AppResources.score + ": " + gc.GetScore();
        }

        void OnContainerSizeChanged(object sender, EventArgs args)
        {
            View container = (View)sender;
            double width = container.Width;
            double height = container.Height;

            if (width <= 0 || height <= 0)
                return;

            // Orient StackLayout based on portrait/landscape mode.
            stackLayout.Orientation = (width < height) ? StackOrientation.Vertical :
                                                         StackOrientation.Horizontal;

            // Calculate tile size and position based on ContentView size.
            tileSize = Math.Min(width, height) / this.sp.width;
            absoluteLayout.WidthRequest = this.sp.width * tileSize;
            absoluteLayout.HeightRequest = this.sp.width * tileSize;

            foreach (View fileView in absoluteLayout.Children)
            {
                SlidingPuzzleTile tile = SlidingPuzzleTile.Dictionary[fileView];

                // Set tile bounds.
                AbsoluteLayout.SetLayoutBounds(fileView, new Rectangle(tile.currentCol * tileSize, tile.currentRow * tileSize, tileSize, tileSize));
            }
        }

        async void OnTileTapped(object sender, EventArgs args)
        {
            if (isBusy)
                return;

            isBusy = true;

            View tileView = (View)sender;
            SlidingPuzzleTile tappedTile = SlidingPuzzleTile.Dictionary[tileView];

            await ShiftIntoEmpty(tappedTile.currentRow, tappedTile.currentCol);
            isBusy = false;
            await isPuzzleSolved();
        }

        private async Task isPuzzleSolved()
        {
            try
            {


                for (int row = 0; row < sp.width; row++)
                {
                    for (int col = 0; col < sp.height; col++)
                    {
                        if (tiles[row, col]!=null && !tiles[row, col].isTilePossitionIsCorrect())
                        {
                            return;
                        }
                    }
                }
            }
            catch(Exception e)
            {
                Console.WriteLine(e.StackTrace);
            }

            scoreLabel.Text = AppResources.score + ": " + gc.EditScore(GameController.SCORE_VALUE.Sliding_Puzzle_Solved);
            gc.FinishAttraction();

            await Navigation.PopModalAsync();
            //TODO puzzle solve
            //DisplayAlert("", "puzzle solved", "OK");
        }

        async Task ShiftIntoEmpty(int tappedRow, int tappedCol, uint length = 100)
        {
            // Shift columns.
            if (tappedRow == emptyRow && tappedCol != emptyCol)
            {
                int inc = Math.Sign(tappedCol - emptyCol);
                int begCol = emptyCol + inc;
                int endCol = tappedCol + inc;

                for (int col = begCol; col != endCol; col += inc)
                {
                    await AnimateTile(emptyRow, col, emptyRow, emptyCol, length);
                }
            }
            // Shift rows.
            else if (tappedCol == emptyCol && tappedRow != emptyRow)
            {
                int inc = Math.Sign(tappedRow - emptyRow);
                int begRow = emptyRow + inc;
                int endRow = tappedRow + inc;

                for (int row = begRow; row != endRow; row += inc)
                {
                    await AnimateTile(row, emptyCol, emptyRow, emptyCol, length);
                }
            }
        }

        async Task AnimateTile(int row, int col, int newRow, int newCol, uint length)
        {
            // The tile to be animated.
            SlidingPuzzleTile tile = tiles[row, col];
            View tileView = tile.TileView;

            // The destination rectangle.
            Rectangle rect = new Rectangle(emptyCol * tileSize,
                                           emptyRow * tileSize,
                                           tileSize,
                                           tileSize);

            // Animate it!
            await tileView.LayoutTo(rect, length);

            // Set layout bounds to same Rectangle.
            AbsoluteLayout.SetLayoutBounds(tileView, rect);

            // Set several variables and properties for new layout.
            tiles[newRow, newCol] = tile;
            tile.currentRow = newRow;
            tile.currentCol = newCol;
            tiles[row, col] = null;
            emptyRow = row;
            emptyCol = col;
        }

        void OnRandomizeButtonClicked(object sender, EventArgs args)
        {
            Button button = (Button)sender;
            button.IsEnabled = false;
            shuffle();
            button.IsEnabled = true;

            
        }

        private async void shuffle() {
            Random rand = new Random();
            isBusy = true;
            for (int i = 0; i < 50; i++)
            {
                await ShiftIntoEmpty(rand.Next(sp.height), emptyCol, 25);
                await ShiftIntoEmpty(emptyRow, rand.Next(sp.width), 25);
            }
            isBusy = false;
        }

        private async void HowToPlay_Button_Clicked(object sender, EventArgs args)
        {
            await Navigation.PushModalAsync(new instructionsPage(sp));
        }



    }
}