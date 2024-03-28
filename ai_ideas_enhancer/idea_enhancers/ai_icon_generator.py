from .ai_enhancer import AIEnhancer 


class AIIconGenerator(AIEnhancer):
    def process(self, idea: str) -> dict[str, str]:
        prompt = f"""
        Project Idea: A platform that uses machine learning to adaptively improve students' understanding of complex math concepts through personalized problem sets.
        Project Icon: 🧮

        Project Idea: A mobile app that optimizes your daily schedule, balancing productivity with well-being by using AI to suggest study times, breaks, and leisure activities.
        Project Icon: 🕒

        Project Idea: An application that teaches music theory through interactive lessons and games, utilizing AI to adapt to the learner's progress and interest.
        Project Icon: 🎼

        Project Idea: {idea}
        Project Icon: 
        """
        
        try:
            return {
                "icon": self._generate(prompt, max_length=2, max_tries=10),
            }
        
        except Exception as e:
            return {
                "icon": input(f"Enter an icon for {idea}: "),
            }
