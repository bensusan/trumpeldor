using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text;
using trumpeldor.SheredClasses;

namespace trumpeldor
{
    public class ServerConnectionForTests : ServerConection
    {
        public User myUser = null;
        public Track shortT = null;
        public Track mediumT = null;
        public Attraction a1 = null;
        public Attraction a2 = null;
        public Trip myTrip = null;

        public ServerConnectionForTests()
        {
            myUser = MakeUser();
            myTrip = MakeTrip();
            a1 = MakeAttractionA();
            a2 = MakeAttractionB();
            shortT = MakeShortTrack(a1);
            mediumT = MakeMediumTrack(shortT, a2);

        }

        private Trip MakeTrip()
        {
            List<Attraction> myAttractionsDone = new List<Attraction>();
            myAttractionsDone.Add(MakeAttractionA());
            List<FeedbackInstance> feedback = new List<FeedbackInstance>();
            feedback.Add(new FeedbackInstance { feedback=new Feedback { id=1, kind= "FT", question="what is your feedback?" }, answer="positive feedback" });
            List<int> myAges = new List<int>();
            myAges.Add(5); myAges.Add(10);
            return new Trip
            {
                attractionsDone = myAttractionsDone,
                feedbacks = feedback,
                groupName = "testGroup",
                id = 1,
                playersAges = myAges,
                score = 40,
                track = new Track { id = 1, length = 1, subTrack = null, points = myAttractionsDone }        
            };
        }
        private User MakeUser()
        {
            return new User
            {
                name = "UserForTests",
                socialNetwork = "",
                email = "",
                lastSeen = null
            };
        }
        private Attraction MakeAttractionA()
        {
            int[] correctIdx = new int[1];
            correctIdx[0] = 1;
            List<string> ans = new List<string>();
            ans.Add("ans1"); ans.Add("ans2"); ans.Add("ans3");
            List<Hint> myHints = new List<Hint>();
            myHints.Add(new Hint { id = 1, data = "this is a text hint for tests", description = "hint description", kind = "HT" });
            List<string> myPicturesUrls = new List<string>();
            myPicturesUrls.Add("https://www.google.com/search?q=xamarin&source=lnms&tbm=isch&sa=X&ved=0ahUKEwizlsTr6LviAhXLKVAKHSR3DTkQ_AUIDigB&biw=1366&bih=657#imgrc=zTNiCHUFG6rAlM:");
            return new Attraction
            {
                americanQuestion=new AmericanQuestion { answers=ans ,id=1, indexOfCorrectAnswer=correctIdx, question="question?" },
                description="description1",
                entertainment=new TakingPicture { description="taking picture description", id=1 },
                hints=myHints,
                id=1,
                name="attraction test 1",
                picturesURLS=myPicturesUrls,
                videosURLS=null,
                visible=true,
                x=1,
                y=1
            };
        }

        private Attraction MakeAttractionB()
        {
            int[] correctIdx = new int[1];
            correctIdx[0] = 1;
            List<string> ans = new List<string>();
            ans.Add("ans1"); ans.Add("ans2"); ans.Add("ans3");
            List<Hint> myHints = new List<Hint>();
            myHints.Add(new Hint { id = 2, data = "this is a text hint for tests2", description = "hint description", kind = "HT" });
            List<string> myPicturesUrls = new List<string>();
            myPicturesUrls.Add("https://www.google.com/search?q=xamarin&source=lnms&tbm=isch&sa=X&ved=0ahUKEwizlsTr6LviAhXLKVAKHSR3DTkQ_AUIDigB&biw=1366&bih=657#imgrc=zTNiCHUFG6rAlM:");
            return new Attraction
            {
                americanQuestion = new AmericanQuestion { answers = ans, id = 2, indexOfCorrectAnswer = correctIdx, question = "question?" },
                description = "description2",
                entertainment = new TakingPicture { description = "taking picture description2", id = 2 },
                hints = myHints,
                id = 2,
                name = "attraction test 2",
                picturesURLS = myPicturesUrls,
                videosURLS = null,
                visible = true,
                x = 2,
                y = 2
            };
        }

        private Track MakeShortTrack(Attraction a1)
        {
            List<Attraction> attractions = new List<Attraction>();
            attractions.Add(a1);
            return new Track
            {
                id = 1,
                length = 1,
                points = attractions,
                subTrack = null
            };
        }

        private Track MakeMediumTrack(Track sub, Attraction a2)
        {
            List<Attraction> attractions = new List<Attraction>();
            attractions.Add(a2);
            return new Track
            {
                id=2,
                length=2,
                points=attractions,
                subTrack=sub
            };
        }

        public StringContent ContentPost(object obj)
        {
            throw new NotImplementedException();
        }

        public Trip CreateTrip(User currentUser, string groupName, List<int> playersAges, int trackLength, double xUser, double yUser)
        {
            //return myTrip;
            List<FeedbackInstance> feedback = new List<FeedbackInstance>();
            feedback.Add(new FeedbackInstance { feedback = new Feedback { id = 1, kind = "FT", question = "what is your feedback?" }, answer = "positive feedback" });
            return new Trip
            {
                user = currentUser,
                groupName = groupName,
                playersAges = playersAges,
                attractionsDone = null,
                track = mediumT,
                id = 1,
                score = 100,
                feedbacks = feedback
            };
            /*Trip trip = new Trip();
            trip.attractionsDone = GetFullAttractions(trip.attractionsDone);
            trip.track = GetFullTrack(trip.track);
            trip.feedbacks = GetFeedbacks(trip);*/
        }

        public AmericanQuestion GetAmericanQuestionByAttraction(Attraction attraction)
        {
            if (attraction.americanQuestion.question.Equals("") && attraction.americanQuestion.answers == null && attraction.americanQuestion.indexOfCorrectAnswer == null)
                return null;
            else return attraction.americanQuestion;
        }

        public Attraction GetAttractionForDebug()
        {
            return MakeAttractionA();
        }

        public List<UserGroupScore> GetBestScoreData()
        {
            throw new NotImplementedException();
        }

        public Track GetExtendedTrack(Track track, Point userLocation)
        {
            throw new NotImplementedException();
        }

        public void GetFullAttraction(Attraction attraction)
        {
            attraction.hints = GetHintsByAttraction(attraction);
            attraction.americanQuestion = GetAmericanQuestionByAttraction(attraction);
            attraction.entertainment = GetEntertainmentByAttraction(attraction);
        }

        public List<Attraction> GetFullAttractions(List<Attraction> attractions)
        {
            throw new NotImplementedException();
        }

        public Track GetFullTrack(Track track)
        {
            throw new NotImplementedException();
        }

        public List<Hint> GetHintsByAttraction(Attraction attraction)
        {
            return attraction.hints;
        }

        public List<OpenMessage> GetOpenMessages()
        {
            List<OpenMessage> lst = new List<OpenMessage>();
            lst.Add(new OpenMessage { data = "message data", title = "current message" });
            return lst;
        }

        public Trip GetPreviousTrip(User currentUser)
        {
            throw new NotImplementedException();
        }

        public Setttings GetSettings()
        {
            List<Point> bounds = new List<Point>();
            bounds.Add(new Point(-2, -2));
            bounds.Add(new Point(2, -2));
            bounds.Add(new Point(-2, 2));
            bounds.Add(new Point(2, 2));
            List<ScoreRule> myRules = new List<ScoreRule>();
            myRules.Add(new ScoreRule { ruleName = "hmtt", score = 10 });
            myRules.Add(new ScoreRule { ruleName = "aqm", score = 20 });
            myRules.Add(new ScoreRule { ruleName = "aqc", score = 30 });
            myRules.Add(new ScoreRule { ruleName = "aa", score = 40 });
            myRules.Add(new ScoreRule { ruleName = "sps", score = 50 });
            myRules.Add(new ScoreRule { ruleName = "ttd", score = 60 });
            myRules.Add(new ScoreRule { ruleName = "ps", score = 70 });
            return new Setttings
            {
                boundaries = bounds,
                loginHours = 36,
                logo = "https://www.google.com/search?q=xamarin&source=lnms&tbm=isch&sa=X&ved=0ahUKEwizlsTr6LviAhXLKVAKHSR3DTkQ_AUIDigB&biw=1366&bih=657#imgrc=dtTlcBS6cgD0HM:",
                scoreRules = myRules
            };
        }

        public RelevantInformation LoadRelevantInformationFromLastTrip(User currentUser)
        {
            List<int> myAges = new List<int>();
            myAges.Add(5); myAges.Add(10);
            return new RelevantInformation
            {
                groupName = "testGroup",
                playersAges = myAges
            };
        }

        public User SignUp(string name, string socialNetwork)
        {
            return new User
            {
                name = name,
                email = "aaa.aaa@aaa",
                lastSeen = null,
                socialNetwork = socialNetwork
            };
        }

        public void UpdateTrip(Trip currentTrip)
        {
            throw new NotImplementedException();
        }

        private Entertainment GetEntertainmentByAttraction(Attraction attraction)
        {
            Entertainment ent = attraction.entertainment;
            if (ent is SlidingPuzzle)
            {
                SlidingPuzzle currEnt = (SlidingPuzzle)ent;
                return new SlidingPuzzle
                {
                    id = currEnt.id,
                    description = currEnt.description,
                    piecesURLS = currEnt.piecesURLS,
                    width = currEnt.width,
                    height = currEnt.height
                };
            }
            else if (ent is Puzzle)
            {
                Puzzle currEnt = (Puzzle)ent;
                return new Puzzle
                {
                    id = currEnt.id,
                    description = currEnt.description,
                    piecesURLS = currEnt.piecesURLS,
                    width = currEnt.width,
                    height = currEnt.height
                };
            }
            else if (ent is TakingPicture)
            {
                TakingPicture currEnt = (TakingPicture)ent;
                return new TakingPicture
                {
                    id = currEnt.id,
                    description = currEnt.description
                };
            }
            return null;
        }

        public bool IsAdmin(string email)
        {
            return false;
        }
    }
}
