using System;
using System.Collections.Generic;
using System.Text;
using trumpeldor.SheredClasses;
using Plugin.Geolocator;
using Xamarin.Forms.Maps;
using System.Threading.Tasks;
using System.IO;
using Xamarin.Forms;
using System.Runtime.CompilerServices;
using System.Timers;
using System.Globalization;

namespace trumpeldor
{
    public class GameController
    {
        //public enum SCORE_VALUE {
        //    Hints_More_Than_Three = -10,
        //    AQ_Mistake = -2,
        //    AQ_Correct = 10,
        //    Attraction_Arrive = 50,
        //    Sliding_Puzzle_Solved = 10,
        //    Taking_Picture_Done = 10,
        //    Puzzle_Solved = 10
        //}

        private static GameController instance = null;

        public Trip currentTrip = null;
        public User currentUser = null; //Also will show in Trip object but necessary also.
        private ServerConection conn;
        public bool isFinishTrip;
        //const int LOGIN_RECENETLY_DIFFERENCE_HOURS = 36; //TODO - Very specific for now
        public Track extendTrack = null;
        public bool isAttractionDone = false;
        public static SheredClasses.Point myLocation;
        //public DateTime? timeOfLocation = null;
        private static double DESIRED_SECONDS = 1;
        private static bool firstTime = true;
        private readonly System.Threading.EventWaitHandle waitHandle = new System.Threading.AutoResetEvent(false);
        private Setttings appSettings;
        private static bool isInTest = false;

        public static GameController getInstance(ServerConnectionForTests sct)
        {
            if (instance == null)
            {
                isInTest = true;
                instance = new GameController(sct);
                myLocation = new SheredClasses.Point(31.262880,34.801722);
            }
            return instance;
        }

        public CultureInfo hebrew = new CultureInfo("he");
        public CultureInfo english = new CultureInfo("en");

        public static GameController getInstance()
        {
            if (instance == null)
            {
                ServerConnectionImpl serverConnection = ServerConnectionImpl.getInstance();
                instance = new GameController(serverConnection);
            }
            return instance;
        }

        public bool IsAdmin(string email)
        {
            return conn.IsAdmin(email);
        }

        public bool IsUserInValidSector()
        {
            SheredClasses.Point currLoc = GetUserLocation();
            //Very specific to BGU!!! TODO CHANGE
            //List<SheredClasses.Point> points = new List<SheredClasses.Point>()
            //{
            //    new SheredClasses.Point(31.265372, 34.798240),
            //    new SheredClasses.Point(31.261009, 34.798178),
            //    new SheredClasses.Point(31.260975, 34.805906),
            //    new SheredClasses.Point(31.263513, 34.805998),
            //    new SheredClasses.Point(31.265315, 34.803155)
            //};
            

            //xMin, xMax, yMin, yMax
            //double[] relevantValues = GetRelevantValuesFromPolygonSector(points);

            double[] relevantValues = GetRelevantValuesFromPolygonSector(appSettings.boundaries);
            if (
                currLoc.x > relevantValues[0] &&
                currLoc.x < relevantValues[1] &&
                currLoc.y > relevantValues[2] &&
                currLoc.y < relevantValues[3])
                return true;
            return false;
        }

        private double[] GetRelevantValuesFromPolygonSector(List<SheredClasses.Point> points)
        {
            double[] ans = new double[4]; //xMin, xMax, yMin, yMax
            foreach (SheredClasses.Point p in points)
            {
                if (p.x < ans[0]) ans[0] = p.x;
                if (p.x > ans[1]) ans[1] = p.x;
                if (p.y < ans[2]) ans[2] = p.y;
                if (p.y > ans[3]) ans[3] = p.y;
            }
            return ans;
        }

        internal void StartTaskLocation()
        {
            if (firstTime)
                FindUserLocation();
                //Task.Run(() => FindUserLocation()).ConfigureAwait(false);
            firstTime = false;
        }

        internal List<Attraction> GetVisitedAttractions()
        {
            List<Attraction> visited = new List<Attraction>(currentTrip.attractionsDone);
            if (!isFinishTrip)
                visited.RemoveAt(visited.Count - 1);
            return visited;
        }

        internal List<OpenMessage> GetOpenMessages()
        {
            return conn.GetOpenMessages();
        }

        internal bool IsNewUser()
        {
            string anonymousString;
            User.SocialNetwork2string.TryGetValue(User.SOCIAL_NETWORK.Anonymous, out anonymousString);
            return currentUser.lastSeen == null || currentUser.socialNetwork.Equals(anonymousString);
        }

        internal int GetScore()
        {
            return currentTrip.score;
        }

        public bool IsUserConnectedRecently()
        {
            return !this.IsNewUser() && 
                (DateTime.Now - (DateTime)currentUser.lastSeen).TotalHours <= appSettings.loginHours;
        }

        internal Attraction GetTempAttraction()
        {
            return conn.GetAttractionForDebug();
        }

        internal RelevantInformation LoadRelevantInformationFromLastTrip()
        {
            return conn.LoadRelevantInformationFromLastTrip(currentUser);
        }

        internal void UpdateTrip()
        {
            this.conn.UpdateTrip(this.currentTrip);
        }

        internal void FinishAttraction()
        {
            isAttractionDone = true;
            SheredClasses.Point currLoc = GetUserLocation();
            isFinishTrip = this.currentTrip.DoneMyAttraction(currLoc.x, currLoc.y);
            UpdateTrip();
        }

        internal void ContinuePreviousTrip()
        {
            this.currentTrip = conn.GetPreviousTrip(currentUser);
            /*
            currentTrip.feedbacks = new List<FeedbackInstance>();
            currentTrip.feedbacks.Add(new FeedbackInstance { feedback = new Feedback { id = 1, kind = "l", question = "MMM" }, answer = "KK" });
            foreach(var a in currentTrip.attractionsDone)
            {
                a.americanQuestion = new AmericanQuestion { id = 5, question = "A", answers = new List<string>(), indexOfCorrectAnswer = new int[1] };
                a.americanQuestion.answers.Add("1");
                a.americanQuestion.answers.Add("2");
                a.americanQuestion.indexOfCorrectAnswer[0] = 1;
                a.hints = new List<Hint>();
                a.hints.Add(new Hint { kind="V", id=1, data="iiiiii", description="....." });
            }
            */
        }

        private GameController(ServerConection serverConnection)
        {
            if (serverConnection is ServerConnectionImpl)
            {
                this.conn = (ServerConnectionImpl)serverConnection;
                appSettings = this.conn.GetSettings();
            }
            else if (serverConnection is ServerConnectionForTests)
            {
                this.conn = (ServerConnectionForTests)serverConnection;
                appSettings = this.conn.GetSettings();
            }
        }

        public void CreateTrip(string groupName, List<int> playersAges, int trackLength)
        {
            SheredClasses.Point currLoc = GetUserLocation();
            currentTrip = conn.CreateTrip(currentUser, groupName, playersAges, trackLength, currLoc.x, currLoc.y);
        }

        public SheredClasses.Point GetUserLocation()
        {
            if (!isInTest)
            {
                waitHandle.WaitOne();
                return myLocation;
            }
            return myLocation;
        }

        private void FindUserLocation()
        {
            //Task.Run(async () =>
            //{
            Timer locationTimer = new Timer();
            locationTimer.Interval = DESIRED_SECONDS * 1000;
            locationTimer.Elapsed += async (o, e) =>
            {
                waitHandle.Reset();
                //Task.Run(async () =>
                //{
                var locator = CrossGeolocator.Current;
                Plugin.Geolocator.Abstractions.Position position = await locator.GetPositionAsync(TimeSpan.FromSeconds(DESIRED_SECONDS));
                myLocation = new SheredClasses.Point(position.Latitude, position.Longitude);
                waitHandle.Set();
                //});
            };
            locationTimer.Start();

            //timeOfLocation = DateTime.Now;
            //});
        }

        //public bool isCurrentLocation()
        //{
        //    return timeOfLocation != null && 
        //        DateTime.Now.Subtract((DateTime)timeOfLocation).TotalSeconds < DESIRED_SECONDS;
        //}

        //get y.png for example return http://IP:PORT/media/y.png
        //public string GetMediaURLFromName(string pictureName)
        //{
        //    return "http://" + ServerConection.IP + ":" + ServerConection.PORT + "/media/" + pictureName;
        //}

        public bool CanContinueToLongerTrack()
        {
            SheredClasses.Point currLoc = GetUserLocation();
            this.extendTrack = conn.GetExtendedTrack(this.currentTrip.track, currLoc);
            return this.extendTrack != null;
        }

        public void ContinueToLongerTrack()
        {
            currentTrip.track = extendTrack;
            SheredClasses.Point currLoc = GetUserLocation();
            isFinishTrip = currentTrip.DoneMyAttraction(currLoc.x, currLoc.y);
            UpdateTrip();
        }

        public void SignUp(string name, string socialNetwork)
        {
            this.currentUser = conn.SignUp(name, socialNetwork);
        }

        public int EditScore(ScoreRule.Kinds actionScore)
        {
            foreach(ScoreRule scoreRule in appSettings.scoreRules)
            {
                if(scoreRule.GetKind() == actionScore){
                    currentTrip.score += scoreRule.score;
                    return currentTrip.score;
                }
            }
            throw new Exception("Score rule does not exist");
        }

        internal List<string> GetMainImages()
        {
            return new List<string>();
        }

        internal List<string> GetMainVideos()
        {
            return new List<string>();
        }

        internal double GetHeightSizeOfPage()
        {
            return Application.Current.MainPage.Height;
        }

        internal double GetWidthSizeOfPage()
        {
            return Application.Current.MainPage.Width;
        }

        internal List<UserGroupScore> GetLeadingTable()
        {
            return conn.GetBestScoreData();
        }

    }
}
