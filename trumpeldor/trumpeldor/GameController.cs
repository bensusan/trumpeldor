using System;
using System.Collections.Generic;
using System.Text;
using trumpeldor.SheredClasses;
using Plugin.Geolocator;
using Xamarin.Forms.Maps;
using System.Threading.Tasks;
using System.IO;

namespace trumpeldor
{
    public class GameController
    {
        //TODO MAKE TRIP INSTEAD OF SCORE, GROUPNAME, USER, TRACK
        public Trip currentTrip = null;
        public User currentUser = null; //Also will show in Trip object but necessary also.
        //public enum PathLength { shortPath = 1, mediumPath = 2, longPath = 3 }
        private ServerConection conn;
        //private String groupName;
        //public int score;
        private Dictionary<Attraction,Boolean> destinations;
        public bool isFinishTrip;
        //private PathLength currentPathLength;
        //public Attraction currentAttractionDestination = null;
        const int LOGIN_RECENETLY_DIFFERENCE_HOURS = 36; //TODO - Very specific for now


        internal int GetScore()
        {
            return currentTrip.score;
        }

        private int GetNextPathLength(int pl)
        {
            return pl + 1;
        }

        public bool IsUserConnectedRecently()
        {
            if (currentUser.lastSeen == null)
                return false;
            var hours = (DateTime.Now - (DateTime)currentUser.lastSeen).TotalHours;
            return hours <= LOGIN_RECENETLY_DIFFERENCE_HOURS;
        }

        internal async Task<KeyValuePair<string, List<int>>> LoadRelevantInformationFromLastTrip()
        {
            return await conn.LoadRelevantInformationFromLastTrip(currentUser);
        }

        internal async Task ContinuePreviousTrip()
        {
            currentTrip = await conn.GetPreviousTrip(currentUser);
        }

        public GameController()
        {
            this.conn = new ServerConection();
            destinations = new Dictionary<Attraction, bool>();
        }

        public async void CreateTrip(string groupName, List<int> playersAges, int trackLength)
        {
            currentTrip = await conn.CreateTripAsync(currentUser, groupName, playersAges, trackLength, GetUserX(), GetUserY());

        }

        private float GetUserY()
        {
            //TODO
            throw new NotImplementedException();
        }

        private float GetUserX()
        {
            //TODO
            throw new NotImplementedException();
        }

        public async void SelectNextAttraction()
        {
            var locator = CrossGeolocator.Current;
            var position = await locator.GetPositionAsync(TimeSpan.FromSeconds(10));
            double latitude = position.Latitude;
            double Longitude = position.Longitude;
           
            Attraction nextAttraction = await conn.GetNextAttraction(currentTrip.id);
            currentTrip.DoneMyAttraction(nextAttraction);
            if (nextAttraction == null)
                isFinishTrip = true;

            //TODO: Trip done - what now
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

        //get y.png for example return http://IP:PORT/media/y.png
        public string GetImageURLFromName(string pictureName)
        {
            return "http://" + ServerConection.IP + ":" + ServerConection.PORT + "/media/" + pictureName;
        }

        public string GetCurrentAttractionImage()
        {
            return GetImageURLFromName(currentTrip.GetCurrentAttraction().GetMainPictureUrl());
        }

        public bool IsCurrentAttractionHasAR()
        {
            //TODO Iteration 2
            return false;
        }

        public String GetGeneralInformation()
        {
            return "some general information";
        }

        public String GetCurrentAttractionQuestion()
        {
            //TODO
            return "choose 1";
        }

        public bool IsCurrentAttractionHasQuestionImage()
        {
            //TODO
            return false;
        }

        public Xamarin.Forms.ImageSource GetCurrentAttractionQuestionImage()
        {
            //TODO
            return null;
        }

        public List<String> GetCurrentAttractionQuestionAnswers()
        {
            //TODO
            List<string> ans = new List<string>();ans.Add("1"); ans.Add("2"); ans.Add("3"); ans.Add("4");
            return ans;
        }

        public int GetCurrentAttractionCurrectAnswersToQuestion()
        {
            //TODO 
            return 0;
        }

        public bool CanContinueToLongerTrack()
        {
            return currentTrip.track.length != 3;
        }

        public void ContinueToLongerTrack()
        {
           
        }

        public List<Attraction> GetVisitedAttractions()
        {
            List<Attraction> visitedAttractions = new List<Attraction>();
            foreach (Attraction Attraction in destinations.Keys)
            {
                if (destinations[Attraction])
                {
                    visitedAttractions.Add(Attraction);
                }
            }
            return visitedAttractions;
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
        private void SelectNextAttractionHelper(double latitude, double longitude)
        {
            double ShortestDistance = double.MaxValue;
            Attraction closestAttraction = null;


            foreach (Attraction tp in destinations.Keys)
            {
                if(!destinations[tp])//we dont visit at tp
                {
                    
                    double distance=GetDistanceFromLatLonInKm(position.Latitude, position.Longitude, tp.GetLatitude(), tp.GetLongitude());
                    if(ShortestDistance > distance)
                    {
                        ShortestDistance = distance;
                        closestAttraction = tp;
                    }
                }
            }
            if (closestAttraction == null) { this.isFinishTrack = true; }
            else
            {
                this.currentAttractionDestination = closestAttraction;
                this.destinations[closestAttraction] = true;
            }
        }*/
        
        public async Task SignUp(string name, string socialNetwork)
        { 
            currentUser = await conn.SignUp(name, socialNetwork);
        }
    }
}
