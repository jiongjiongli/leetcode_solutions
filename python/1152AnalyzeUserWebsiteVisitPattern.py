class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # 1. Group websites by username
        website_infos = {}
        for user, visit_time, web in zip(username, timestamp, website):
            website_info = (visit_time, web)
            website_infos.setdefault(user, [])
            website_infos[user].append(website_info)

        # 2. Sort websites by time
        websites = {}
        for user, infos in website_infos.items():
            infos.sort(key=lambda website_info: website_info[0])
            websites[user] = [website_info[1] for website_info in infos]

        # 3. Collect patterns per user
        user_patterns = {}
        for user, webs in websites.items():
            patterns = set()
            for i in range(len(webs)):
                for j in range(i + 1, len(webs)):
                    for k in range(j + 1, len(webs)):
                        pattern = (webs[i], webs[j], webs[k])
                        patterns.add(pattern)

            user_patterns[user] = patterns

        # 4. Get pattern counts
        pattern_counts = {}
        for user, patterns in user_patterns.items():
            for pattern in patterns:
                pattern_counts.setdefault(pattern, 0)
                pattern_counts[pattern] += 1

        # 5. Find max pattern count
        best_pattern = None
        max_count = 0

        for pattern, count in pattern_counts.items():
            if count > max_count:
                max_count = count
                best_pattern = pattern

            elif count == max_count and pattern < best_pattern:
                best_pattern = pattern

        return list(best_pattern)

