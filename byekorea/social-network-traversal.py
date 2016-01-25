import operator

# Amazon problem
# Each person has his attended course and his direct friend
# Get course list to attend recommended by close frineds (should be sorted. sort by attend count)
# (close friends : consider until 2 depth direct friends)

# Problem offers two functions below
# getDirectFriendsForUser(userID)
# getAttendedCoursesForUser(userID)

def getDirectFriendsForUser(userID):
    return []
def getAttendedCoursesForUser(userID):
    return []

def getUserCourses(userID):

    # collect direct friends
    directFriendsDic = {}
    firstDepthFriends = getDirectFriendsForUser(userID)
    for fid in firstDepthFriends:
        directFriendsDic[fid] = True
        secondDepthFriends = getDirectFriendsForUser(fid)
        for fid2 in secondDepthFriends:
            directFriendsDic[fid2] = True
    del directFriendsDic[userID]  # exclude myself

    # collect courses
    courses = {}  # dic[courseID] = attend count of all direct frineds
    for fid, val in directFriendsDic.items():
        fcourses = getAttendedCoursesForUser(fid)
        for cid in fcourses:
            if cid in courses:
                courses[cid] += 1
            else:
                courses[cid] = 1

    sortedByValue = sorted(courses.items(), key=operator.itemgetter(1), reverse=True)
    retList = []
    for courseKey in sortedByValue :
        retList.append(courseKey)

    return retList