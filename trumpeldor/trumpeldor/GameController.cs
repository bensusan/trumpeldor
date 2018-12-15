using System;
using System.Collections.Generic;
using System.Text;
using trumpeldor.SheredClasses;
using Plugin.Geolocator;
using Xamarin.Forms.Maps;

namespace trumpeldor
{
    public class GameController
    {
        public enum PathLength
        {
            shortPath = 1,
            mediumPath = 2,
            longPath = 3
        }
        private PathLength GetNextPathLength(PathLength pl)
        {
            //problem in longPath
            return (PathLength)(((int)pl)+1);
        }

        private ServerConection conn;
        private String groupName;
        private int score;
        private Dictionary<TrackPoint,Boolean> destinations;
        private bool isFinishTrack;
        private PathLength currentPathLength;
        private TrackPoint currentTrackPointDestination = null;


        public GameController()
        {
            this.conn = new ServerConection();
            this.score = 0;
            destinations = new Dictionary<TrackPoint, bool>();
        }

        public void CreateGroup(string groupName, List<int> agesList)
        {
            this.groupName = groupName;
            //TODO
        }

        public int GetScore()
        {
            return this.score;
        }

        public void SelectPath(PathLength selectedPathLength)
        {
            List<TrackPoint>newDestinations= new List<TrackPoint>(){new TrackPoint(31.262485, 34.803953),new TrackPoint(31.261930, 34.804132)};

            //TODO
            foreach (TrackPoint dest in newDestinations)
            {
                this.destinations.Add(dest,false);
            }
            this.isFinishTrack = false;
            this.currentPathLength = selectedPathLength;


        }
        public async void SelectNextTrackPoint()
        {
            
            var locator = CrossGeolocator.Current;
            var position = await locator.GetPositionAsync(TimeSpan.FromSeconds(10));
            double latitude = position.Latitude;
            double Longitude = position.Longitude;

            this.isFinishTrack = true;
            if (this.currentTrackPointDestination != null)
            {
                destinations[this.currentTrackPointDestination] = true;
            }
            foreach (TrackPoint tp in destinations.Keys)
            {
                if (!destinations[tp]) {
                    this.currentTrackPointDestination = tp;
                    this.isFinishTrack = false;
                    break;
                }
            }
            
            //SelectNextTrackPointHelper(latitude, Longitude);
            //TODO 
        }

        

        public Clue GetFisrtHint()
        {
            //TODO
            return new TextClue();
        }
        public Clue GetHint()
        {
            //TODO
            return new TextClue();
        }
        public bool IsCurrentTrackPointHasImage()
        {
            //TODO
            return false;
        }

        public String GetCurrentTrackPointName()
        {
            return this.currentTrackPointDestination.GetName();
        }

        public Xamarin.Forms.ImageSource GetCurrentTrackPointImage()
        {
            //TODO
            return null;
        }
        public bool IsCurrentTrackPointHasAR()
        {
            //TODO
            return false;
        }

        public String GetGeneralInformation()
        {
            return "some general information";
        }

        public String GetCurrentTrackPointQuestion()
        {
            //TODO
            return "choose 1";
        }
        public bool IsCurrentTrackPointHasQuestionImage()
        {
            //TODO
            return false;
        }
        public Xamarin.Forms.ImageSource GetCurrentTrackPointQuestionImage()
        {
            //TODO
            return null;
        }

        public List<String> GetCurrentTrackPointQuestionAnswers()
        {
            //TODO
            List<string> ans = new List<string>();ans.Add("1"); ans.Add("2"); ans.Add("3"); ans.Add("4");
            return ans;
        }

        public int GetCurrentTrackPointCurrectAnswersToQuestion()
        {
            //TODO 
            return 0;
        }

        public bool GetIsFinishTrack()
        {
            return this.isFinishTrack;
        }

        public bool CanContinueToLongerTrack()
        {
            return this.currentPathLength != PathLength.longPath;
        }

        public void ContinueToLongerTrack()
        {
            switch (this.currentPathLength)
            {
                case PathLength.shortPath:
                    SelectPath(PathLength.mediumPath);
                    break;
                case PathLength.mediumPath:
                    SelectPath(PathLength.longPath);
                    break;
            }
        }
        public List<TrackPoint> GetVisitedTrackPoints()
        {
            List<TrackPoint> visitedTrackPoints = new List<TrackPoint>();
            foreach (TrackPoint trackPoint in destinations.Keys)
            {
                if (destinations[trackPoint])
                {
                    visitedTrackPoints.Add(trackPoint);
                }
            }
            return visitedTrackPoints;
        }



        /*private double GetDistanceFromLatLonInKm(double lat1, double lon1, double lat2, double lon2)
        {
            double R = 6371; // Radius of the earth in km
            double dLat = Deg2rad(lat2 - lat1);  // deg2rad below
            double dLon = Deg2rad(lon2 - lon1);
            double a =
              Math.Sin(dLat / 2) * Math.Sin(dLat / 2) +
              Math.Cos(Deg2rad(lat1)) * Math.Cos(Deg2rad(lat2)) *
              Math.Sin(dLon / 2) * Math.Sin(dLon / 2);
            double c = 2 * Math.Atan2(Math.Sqrt(a), Math.Sqrt(1 - a));
            double d = R * c; // Distance in km
            return d;
        }
        private double Deg2rad(double deg)
        {
            return deg * (Math.PI / 180);
        }
        private void SelectNextTrackPointHelper(double latitude, double longitude)
        {
            double ShortestDistance = double.MaxValue;
            TrackPoint closestTrackPoint = null;


            foreach (TrackPoint tp in destinations.Keys)
            {
                if(!destinations[tp])//we dont visit at tp
                {
                    
                    double distance=GetDistanceFromLatLonInKm(position.Latitude, position.Longitude, tp.GetLatitude(), tp.GetLongitude());
                    if(ShortestDistance > distance)
                    {
                        ShortestDistance = distance;
                        closestTrackPoint = tp;
                    }
                }
            }
            if (closestTrackPoint == null) { this.isFinishTrack = true; }
            else
            {
                this.currentTrackPointDestination = closestTrackPoint;
                this.destinations[closestTrackPoint] = true;
            }
        }*/

    }
}
