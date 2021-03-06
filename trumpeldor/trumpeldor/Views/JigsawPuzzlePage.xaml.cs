﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using trumpeldor.ViewModels;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;
using trumpeldor.SheredClasses;
using Rg.Plugins.Popup.Services;

namespace trumpeldor.Views
{
    public partial class JigsawPuzzlePage : ContentPage
    {
        private double tileSize;
        //private int width = 4;
        private List<JigsawTile> tiles;
        private Puzzle puzzle;
        private GameController gc;
        private Attraction attraction;

        public JigsawPuzzlePage(Puzzle puzzle, Attraction attraction)
        {
            InitializeComponent();
            gc = GameController.getInstance();
            subtitles.Source = ServerConection.URL_MEDIA + "subtitles.jpg";
            info.Source = ServerConection.URL_MEDIA + "info.jpg";
            playVideo.Source = ServerConection.URL_MEDIA + "playVideo.jpg";
            scoreLabel.Text = AppResources.score + ": " + gc.GetScore();
            how.Source = ServerConection.URL_MEDIA + "how.png";
            this.puzzle = puzzle;
            tiles = new List<JigsawTile>();
            this.attraction = attraction;

            for (int row = 0; row < puzzle.width; row++)
            {
                for (int col = 0; col < puzzle.height; col++)
                {
                    JigsawTile tile = new JigsawTile(row, col, puzzle.piecesURLS[row * puzzle.width + col]);

                    PanGestureRecognizer panGestureRecognizer = new PanGestureRecognizer();
                    panGestureRecognizer.PanUpdated += OnTilePanUpdated;
                    tile.TileView.GestureRecognizers.Add(panGestureRecognizer);

                    tiles.Add(tile);
                    absoluteLayout.Children.Add(tile.TileView);
                }
            }
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
            tileSize = Math.Min(width, height) / this.puzzle.width;
            absoluteLayout.WidthRequest = this.puzzle.width * tileSize;
            absoluteLayout.HeightRequest = this.puzzle.width * tileSize;

            Random random = new Random();
            foreach (View fileView in absoluteLayout.Children)
            {
                JigsawTile tile = JigsawTile.Dictionary[fileView];

                AbsoluteLayout.SetLayoutBounds(fileView, new Rectangle(random.NextDouble() * ((this.puzzle.width - 1) * tileSize),
                                        random.NextDouble() * ((this.puzzle.width - 1) * tileSize), tileSize, tileSize));
            }
        }

        void OnTilePanUpdated(object sender, PanUpdatedEventArgs e)
        {
            View tileView = (View)sender;
            JigsawTile tile = JigsawTile.Dictionary[tileView];
            if (tile.isSetOnPossition)
            {
                return;
            }

            double newXPosition = getXPositionOfTile(e, tileView);
            if (!(newXPosition <= 0 || newXPosition >= Math.Abs(tileSize - absoluteLayout.WidthRequest)))
            {
                tileView.TranslationX = tileView.TranslationX + e.TotalX;
            }

            double newYPosition = getYPositionOfTile(e, tileView);
            if (!(newYPosition <= 0 || newYPosition >= Math.Abs(tileSize - absoluteLayout.HeightRequest)))
            {
                tileView.TranslationY = tileView.TranslationY + e.TotalY;
            }

            double xDeltaFromCorrectPossition = Math.Abs(tileSize * tile.correctCol - newXPosition);
            double yDeltaFromCorrectPossition = Math.Abs(tileSize * tile.correctRow - newYPosition);

            if (xDeltaFromCorrectPossition < 3 && yDeltaFromCorrectPossition < 3)
            {
                tileView.TranslationX = tileSize * tile.correctCol - tileView.X;
                tileView.TranslationY = tileSize * tile.correctRow - tileView.Y;
                absoluteLayout.LowerChild(tileView);
                tile.isSetOnPossition = true;
                isPuzzleSolvedAsync();
            }
        }

        private async Task isPuzzleSolvedAsync()
        {
            foreach (JigsawTile tile in tiles)
            {
                if (tile != null && !tile.isSetOnPossition)
                {
                    return;
                }
            }
            //TODO puzzle solve
            scoreLabel.Text = AppResources.score + ": " + gc.EditScore(ScoreRule.Kinds.Puzzle_Solved);
            gc.FinishAttraction();
            await Navigation.PopModalAsync();
        }

        private static double getYPositionOfTile(PanUpdatedEventArgs e, View tileView)
        {
            return tileView.Y + tileView.TranslationY + e.TotalY;
        }

        private static double getXPositionOfTile(PanUpdatedEventArgs e, View tileView)
        {
            return tileView.X + tileView.TranslationX + e.TotalX;
        }

        private async void HowToPlay_Button_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new instructionsPage(puzzle));
        }

        private async void PlayVideo_Clicked(object sender, EventArgs e)
        {
            if (attraction.videosURLS.Count > 0)
                await Navigation.PushModalAsync(new ShowVideoAndTextPage(attraction.videosURLS[0], true));
        }

        private async void Subtitles_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new ShowVideoAndTextPage("", false));
        }

        private void Information_Button_Clicked(object sender, EventArgs e)
        {

        }
    }
}