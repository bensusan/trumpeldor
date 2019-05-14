using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using trumpeldor.SheredClasses;
using System.Configuration;
using System.Threading;
using trumpeldor.Configuration;
using Newtonsoft.Json.Linq;

namespace trumpeldor
{
    class ServerConection
    {
        private static ServerConection instance = null;
        //public readonly static string IP = "132.72.23.64";
        //public readonly static string IP = GetIP().Result;
        //public readonly static string PORT = "12345";
        //private readonly String urlPrefix = "http://" + IP +":" + PORT + "/usersystem/";
        public static string IP;
        public static string PORT;
        public static int DEBUG;
        public static string URL_MEDIA;
        private string urlPrefix;

        private static int MAX_TRIES_POST = 1;
        private static int MAX_TRIES_GET = 3;

        public static ServerConection getInstance()
        {
            if (instance == null)
            {
                using (var cts = new CancellationTokenSource())
                {
                    var t = Task.Run(async () => await ConfigurationManager.Instance.GetAsync(cts.Token));
                    t.Wait();
                    var config = t.Result;
                    IP = config.IP;
                    PORT = config.PORT;
                    DEBUG = config.DEBUG;
                    URL_MEDIA = "http://" + ServerConection.IP + ":" + ServerConection.PORT + "/media/";
                }
                instance = new ServerConection();
            }
            return instance;
        }

        private ServerConection()
        {
            urlPrefix = "http://" + IP + ":" + PORT + "/usersystem/";
        }

        public User SignUp(String name, String socialNetwork) {
            var newUser = new
            {
                name = name,
                socialNetwork = socialNetwork,
            };
            string jsonResponse = SendToServerAndGetResponseBack(newUser, "signUp/");
            return JsonConvert.DeserializeObject<User>(jsonResponse);
        }

        internal RelevantInformation LoadRelevantInformationFromLastTrip(User currentUser)
        {
            string jsonResponse = SendToServerAndGetResponseBack(currentUser, "getRelevantPreviousTripInformation/");
            return JsonConvert.DeserializeObject<RelevantInformation>(jsonResponse);
        }

        internal Attraction GetAttractionForDebug()
        {
            string jsonResponse = GetFromServer("getAttractionForDebug/");
            Attraction toReturn = JsonConvert.DeserializeObject<Attraction>(jsonResponse);
            GetFullAttraction(toReturn);
            return toReturn;
        }

        internal void UpdateTrip(Trip currentTrip)
        {
            SendToServerAndGetResponseBack(currentTrip, "updateTrip/");
        }

        internal void GetFullAttraction(Attraction attraction)
        {
            var t1 = Task.Run(() =>
            {
                attraction.hints = GetHintsByAttraction(attraction);
            });
            var t2 = Task.Run(() =>
            {
                attraction.americanQuestion = GetAmericanQuestionByAttraction(attraction);
            });
            var t3 = Task.Run(() =>
            {
                attraction.entertainment = GetEntertainmentByAttraction(attraction);
            });
            t1.Wait(); t2.Wait(); t3.Wait();
            //attraction.hints = GetHintsByAttraction(attraction);
            //attraction.americanQuestion = GetAmericanQuestionByAttraction(attraction);
            //attraction.entertainment = GetEntertainmentByAttraction(attraction);
        }

        private Entertainment GetEntertainmentByAttraction(Attraction attraction)
        {
            string jsonResponse = SendToServerAndGetResponseBack(new { id = attraction.id, }, "getEntertainment/");
            if (jsonResponse.Equals(""))
                return null;
            JObject json = JObject.Parse(jsonResponse);
            string className = (string)json["className"];
            JObject obj = (JObject)json["object"];
            if (SlidingPuzzle.isMyClassName(className)) {
                return new SlidingPuzzle
                {
                    id = (int)obj["id"],
                    description = (string)obj["description"],
                    piecesURLS = ((JArray)obj["piecesURLS"]).ToObject<List<string>>(),
                    width = (int)obj["width"],
                    height = (int)obj["height"]
                };
            }
            else if (Puzzle.isMyClassName(className)){
                return new Puzzle
                {
                    id = (int)obj["id"],
                    description = (string)obj["description"],
                    piecesURLS = ((JArray)obj["piecesURLS"]).ToObject<List<string>>(),
                    width = (int)obj["width"],
                    height = (int)obj["height"]
                };
            }
            else if(TakingPicture.isMyClassName(className))
            {
                return new TakingPicture
                {
                    id = (int)obj["id"],
                    description = (string)obj["description"]
                };
            }
            return null;
        }

        private class HelpHints
        {
            public List<Hint> hints { get; set; }
        }

        internal List<Hint> GetHintsByAttraction(Attraction attraction)
        {
            string jsonResponse = SendToServerAndGetResponseBack(new { id = attraction.id, }, "getHints/");
            jsonResponse = "{ 'hints': " + jsonResponse + "}";
            return JsonConvert.DeserializeObject<HelpHints>(jsonResponse).hints;
        }

        internal AmericanQuestion GetAmericanQuestionByAttraction(Attraction attraction)
        {
            string jsonResponse = SendToServerAndGetResponseBack(new { id = attraction.id, }, "getAmericanQuestion/");
            if (jsonResponse.Equals("{\"question\":\"\",\"answers\":null,\"indexOfCorrectAnswer\":null}"))
                return null;
            return JsonConvert.DeserializeObject<AmericanQuestion>(jsonResponse);
        }

        class HelpFeedbacks
        {
            public List<FeedbackInstance> feedbacks { get; set; }
        }

        private List<FeedbackInstance> GetFeedbacks(Trip trip)
        {
            string jsonResponse = SendToServerAndGetResponseBack(new { id = trip.id, }, "getFeedbackInstances/");
            jsonResponse = "{ 'feedbacks': " + jsonResponse + "}";
            HelpFeedbacks hf = JsonConvert.DeserializeObject<HelpFeedbacks>(jsonResponse);
            return hf.feedbacks;
        }

        internal Trip CreateTrip(User currentUser, string groupName, List<int> playersAges, int trackLength, double xUser, double yUser)
        {
            var toSend = new { user = currentUser, groupName = groupName, playersAges = playersAges, trackLength = trackLength, x = xUser, y = yUser, };
            string jsonResponse = SendToServerAndGetResponseBack(toSend, "createTrip/");
            Trip trip = JsonConvert.DeserializeObject<Trip>(jsonResponse);
            var t1 = Task.Run(() => { trip.attractionsDone = GetFullAttractions(trip.attractionsDone); });
            var t2 = Task.Run(() => { trip.track = GetFullTrack(trip.track); });
            var t3 = Task.Run(() => { trip.feedbacks = GetFeedbacks(trip); });
            t1.Wait(); t2.Wait(); t3.Wait();
            //trip.attractionsDone = GetFullAttractions(trip.attractionsDone);
            //trip.track = GetFullTrack(trip.track);
            //trip.feedbacks = GetFeedbacks(trip);
            return trip;
        }

        internal Track GetExtendedTrack(Track track, SheredClasses.Point userLocation)
        {
            string jsonResponse = SendToServerAndGetResponseBack(new { trackId = track.id, x = userLocation.x, y = userLocation.y,}, "getExtendedTrack/");
            return GetFullTrack(JsonConvert.DeserializeObject<Track>(jsonResponse));
        }

        internal Track GetFullTrack(Track track)
        {
            if (track == null)
                return null;
            Task t = null;
            if (track.subTrack != null)
                t = Task.Run(() => { track.subTrack = GetFullTrack(track.subTrack); });
            track.points = GetFullAttractions(track.points);
            if (track.subTrack != null)
                t.Wait();
            return track;
        }

        internal List<Attraction> GetFullAttractions(List<Attraction> attractions)
        {
            List<Task> tasks = new List<Task>();
            foreach (Attraction attraction in attractions)
                tasks.Add(Task.Run(() => { GetFullAttraction(attraction); }));
            foreach (Task t in tasks)
                t.Wait();
            return attractions;
        }

        internal Trip GetPreviousTrip(User currentUser)
        {
            string jsonResponse = SendToServerAndGetResponseBack(currentUser, "previousTrip/");
            return JsonConvert.DeserializeObject<Trip>(jsonResponse);
        }

        class HelpOpenMessages
        {
            public List<OpenMessage> messages { get; set; }
        }

        internal List<OpenMessage> GetOpenMessages()
        {
            string jsonResponse = GetFromServer("getOpenMessages/");
            jsonResponse = "{ 'messages': " + jsonResponse + "}";
            return JsonConvert.DeserializeObject<HelpOpenMessages>(jsonResponse).messages;
        }

        class HelpUserGroupScore
        {
            public List<UserGroupScore> userGroupScores { get; set; }
        }

        internal List<UserGroupScore> GetBestScoreData()
        {
            string jsonResponse = GetFromServer("getBestScores/");
            jsonResponse = "{ 'userGroupScores': " + jsonResponse + "}";
            return JsonConvert.DeserializeObject<HelpUserGroupScore>(jsonResponse).userGroupScores;
        }


        public StringContent ContentPost(Object obj)
        {
            var json = JsonConvert.SerializeObject(obj);
            var content = new StringContent(json, Encoding.UTF8, "application/json");
            return content;
        }

        private string SendToServerAndGetResponseBack(Object toSend, string endOfUri)
        {
            string ans = "";
            bool error = true;
            int numOfTries = 0;
            Exception lastException = null;

            var content = ContentPost(toSend);
            var uri = urlPrefix + endOfUri;

            using (var client = new HttpClient())
            {
                while (error && numOfTries < MAX_TRIES_POST)
                {
                    try
                    {
                        //var t1 = Task.Run(async () => await client.PostAsync(uri, content));
                        //t1.Wait();
                        //var response = t1.Result;
                        //response.EnsureSuccessStatusCode();
                        //var t2 = Task.Run(async () => await response.Content.ReadAsStringAsync());
                        //ans = t2.Result;
                        Task.Run(async () =>
                        {
                            var response = await client.PostAsync(uri, content);
                            response.EnsureSuccessStatusCode();
                            ans = await response.Content.ReadAsStringAsync();
                        }).Wait();
                        
                        error = false;
                    }
                    catch (Exception e)
                    {
                        numOfTries++;
                        lastException = e;
                    }
                }
            }
            if (error)
                throw lastException;
            return ans;
        }

        private string GetFromServer(string endOfUri)
        {
            string ans = "";
            bool error = true;
            int numOfTries = 0;
            Exception lastException = null;

            var uri = urlPrefix + endOfUri;

            using (var client = new HttpClient())
            {
                while (error && numOfTries < MAX_TRIES_GET)
                {
                    try
                    {
                        //var t = Task.Run(async () => await client.GetStringAsync(uri));
                        //t.Wait();
                        //ans = t.Result;
                        Task.Run(async () => { ans = await client.GetStringAsync(uri); }).Wait();
                        error = false;
                    }
                    catch (Exception e)
                    {
                        numOfTries++;
                        lastException = e;
                    }
                }
            }
            if (error)
                throw lastException;
            return ans;
        }
    }
}
