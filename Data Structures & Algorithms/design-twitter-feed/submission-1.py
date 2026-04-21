class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followerMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count+=1
        self.tweetMap[userId].append((-self.count, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        users = self.followerMap[userId] | {userId}

        for uid in users:
            tweets.extend(self.tweetMap[uid])
            top_tweets = heapq.nsmallest(10, tweets)
        return [tweetId for _, tweetId in top_tweets]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followerMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].discard(followeeId)
        
