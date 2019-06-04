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
    public interface ServerConection
    {
        User SignUp(String name, String socialNetwork);

        RelevantInformation LoadRelevantInformationFromLastTrip(User currentUser);

        Attraction GetAttractionForDebug();

        void UpdateTrip(Trip currentTrip);

        void GetFullAttraction(Attraction attraction);

        Setttings GetSettings();

        List<Hint> GetHintsByAttraction(Attraction attraction);

        AmericanQuestion GetAmericanQuestionByAttraction(Attraction attraction);

        Trip CreateTrip(User currentUser, string groupName, List<int> playersAges, int trackLength, double xUser, double yUser);

        Track GetExtendedTrack(Track track, SheredClasses.Point userLocation);

        Track GetFullTrack(Track track);

        List<Attraction> GetFullAttractions(List<Attraction> attractions);

        Trip GetPreviousTrip(User currentUser);

        List<OpenMessage> GetOpenMessages();

        List<UserGroupScore> GetBestScoreData();

        StringContent ContentPost(Object obj);

        bool IsAdmin(string email);

    }
}
