import json
from datetime import datetime
import re

with open("www.facebook.com.har", encoding="utf-8") as f:
    data = json.load(f)

# with open("chikus2.har", encoding="utf-8") as f:
#     data = json.load(f)

def uni_to_normal(unix_timestamp):
    
        date_time = datetime.fromtimestamp(unix_timestamp)
        return date_time

data = data['log']['entries']


#post version 1 timeline_list_feed_units
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['content']['story']['message']['text'] post text
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['context_layout']['story']['comet_sections']['metadata'][0]['story']['creation_time'] post creation time
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['context_layout']['story']['comet_sections']['metadata'][0]['story']['url'] post url
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['content']['story']['attached_story']['message']['text'] attachment text
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['content']['story']['attached_story']['actors']['name'] attachment names
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['post_id'] post id

    #comments 
    #obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['feedback_target_with_context']['comet_ufi_summary_and_actions_renderer']['feedback']['reaction_count']['count'] number of reactions
    #obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['feedback_target_with_context']['comment_rendering_instance']['comments']['total_count'] number of comments
    #obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['body']['text'] comment text
    #obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['created_time'] time of creation of comment
    #obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['feedback']['plugins'][0]['post_id'] post id of the comment
    #obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['comment_action_links'][0]['comment']['url'] comment url
    #obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['author']['name'] author's name
    #obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['relevant_contextual_replies']['nodes'][0]['comment']['author']['name'] reply author's name
    #obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['relevant_contextual_replies']['nodes'][0]['comment']['body']['text'] reply to comment text

#post version 2 ['data']['node']
#obj['data']['node']['post_id'] post id
#obj['data']['node']['comet_sections']['content']['story']['message']['text'] post text
#obj['data']['node']['comet_sections']['content']['story']['attached_story']['actors'][0]['name'] #attachment names
#obj['data']['node']['comet_sections']['content']['story']['attached_story']['message']['text'] attachment text
#obj['data']['node']['attached_story']['comet_sections']['context_layout']['story']['comet_sections']['metadata'][0]['story']['url'],'kkk') attached story url
#obj['data']['node']['attached_story']['comet_sections']['context_layout']['story']['comet_sections']['metadata'][0]['story']['creation_time'],'uuu') attached story creation time
#obj['data']['node']['comet_sections']['content']['story']['message']['text'] #post text
#obj['data']['node']['comet_sections']['context_layout']['story']['comet_sections']['metadata'][0]['story']['creation_time'] post creation time
#obj['data']['node']['comet_sections']['context_layout']['story']['comet_sections']['metadata'][0]['story']['url'] post url
#names of people with whom rhodes must fall made the post:
#obj['data']['node']['comet_sections']['context_layout']['story']['comet_sections']['title']['story']['title']['aggregated_ranges'][0]['sample_entities'] 
            #for x in obj['data']['node']['comet_sections']['context_layout']['story']['comet_sections']['title']['story']['title']['aggregated_ranges'][0]['sample_entities']:
                #print(x['name'])
    #comments 
    #obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['feedback_target_with_context']['comment_rendering_instance']['comments']['total_count'] #number of comments
    #obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['feedback_target_with_context']['comet_ufi_summary_and_actions_renderer']['feedback']['reaction_count']['count'] number of reactions
    #obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['body']['text'] comment text
    #obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['author']['name'] author's name
    #obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['created_time'] time of creation
    #obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['user']['name'] author's name
    #obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['comment_action_links'][0]['comment']['url'] comment url
    #obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['relevant_contextual_replies']['nodes'][0]['comment']['body']['text'] reply to comment text
    #obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['relevant_contextual_replies']['nodes'][0]['comment']['user']['name'] reply author's name
    #obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['relevant_contextual_replies']['nodes'][0]['comment']['author']['name'] reply author's name
    #obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['feedback']['plugins'][0]['post_id'] post id of the comment
    


#rubbish 
# obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['content']['story']['comet_sections']['message'] same as the above
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['content']['story']['actors'] is useless
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['content']['story']['feedback'] is useless
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['content']['story']['encrypted_tracking'] is useless
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['content']['story']['attachments'] is useless
# obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['content']['story']['sponsored_data'] is useless
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['content']['story']['text_format_metadata'] is useless
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['content']['story']['ghl_label_mocked_cta_button'] is useless
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['content']['story']['wwwURL'] is useless
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['content']['story']['target_group'] is useless
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['content']['story']['attached_story']['attachments'][0] idk, seems useless
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['header'] is useless
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['footer'] /post_inform_treatment/outer_footer are useless
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['debug_info'] is useless
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['future_of_feed_info'] 
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['whatsapp_ad_context']
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['viewability_config']
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['post_inform_treatment']
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['footer']
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['__typename']
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['layout']
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['content']['story']['attached_story']['comet_sections']
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['content']['story']['attached_story']
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['content']['__typename']
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['content']['__module_component_CometFeedStoryContentMatchRenderer_story']
#obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['content']['__module_operation_CometFeedStoryContentMatchRenderer_story']
#obj['data']['node']['feedback']
#obj['data']['node']['is_story_civic']
#obj['data']['node']['comet_sections']['context_layout']['story']['comet_sections']['actor_photo']
#obj['data']['node']['comet_sections']['context_layout']['story']['comet_sections']['title']['story']['comet_sections']
#obj['data']['node']['comet_sections']['context_layout']['story']['easy_hide_button_story']
#obj['data']['node']['comet_sections']['context_layout']['story']['can_viewer_see_menu']
#obj['data']['node']['comet_sections']['context_layout']['story']['serialized_frtp_identifiers']
#obj['data']['node']['comet_sections']['context_layout']['__module_operation_CometFeedStoryContextSectionMatchRenderer_story']
#obj['data']['node']['comet_sections']['context_layout']['__module_component_CometFeedStoryContextSectionMatchRenderer_story']
#obj['data']['node']['comet_sections']['context_layout']['__isICometStorySection']
#obj['data']['node']['comet_sections']['context_layout']['__typename']
#obj['data']['node']['comet_sections']['context_layout']['is_prod_eligible']
#obj['data']['node']['comet_sections']['context_layout']['local_alerts_story_menu_promotion']
#obj['data']['node']['comet_sections']['context_layout']['is_regulation_enforced'].
#obj['data']['node']['__module_operation_CometFeedUnitContainerSection_feedUnit']
#obj['data']['node']['__module_component_CometFeedUnitContainerSection_feedUnit']
#obj['data']['node']['viewability_config']
#obj['data']['node']['__isTrackableFeedUnit']
#obj['data']['node']['trackingdata'] 
#obj['data']['node']['schema_context']
#obj['data']['node']['bumpers']
#obj['data']['node']['matched_terms']
#obj['data']['node']['__isFeedUnit']
#obj['data']['node']['should_host_actor_link_in_watch']
#obj['data']['node']['comet_sections']['feedback']['story']['feedback_context']
#obj['data']['node']['comet_sections']['feedback']['story']['id']
# obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['__typename']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['__module_operation_CometFeedUFIContainer_story']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['__module_component_CometFeedUFIContainer_story']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['depth']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['legacy_fbid']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['parent_post_story']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['inline_replies_expander_renderer']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['parent_feedback']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['comment_parent']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['elevated_comment_data'] 
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['is_viewer_comment_poster']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['attachments']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['group_comment_info']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['bizweb_comment_info']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['if_viewer_can_see_member_page_tooltip']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['comment_action_links']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['question_and_answer_type']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['comment_menu_tooltip']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['spam_display_mode']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['work_answered_event_comment_renderer']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['community_comment_signal_renderer']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['business_comment_attributes']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['discoverable_identity_badges_web']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['__module_operation_useCometUFIAdaptivePostActionBar_story']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['__module_component_useCometUFIAdaptivePostActionBar_story']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['vote_attachments']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['target_group']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['inform_treatment_for_messaging']
#obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['sponsored_data']
count=0
content="["

for x in data:
    if "https://www.facebook.com/api/graphql/" == x['request']['url']:
        try:
            response = x['response']['content']['text'].replace('\n', '')
            
            content=content+response.replace('\\"','')+","
        except Exception as e:
            pass



content=content.rstrip(",")+"]"
content=re.compile('}\s*{').sub('},{', content)

posts = json.loads(content)
count=0
count1=0
all_data = []

columns=['post_id','post_text','post_creation_time','post_url','attachment_text','attachment_names','number_of_reactions','number_of_comments','comment_text','comment_creation_time','comment_author','comment_url','reply_to_comment_text','reply_author_name','comment_post_id']





#####################
import re

#path finder, finds a dic path to a string value
def find_string_path(d, target, path=None):
    if path is None:
        path = []
        
    for key, value in d.items():
        current_path = path + [key]  # Update path with the current key

        if isinstance(value, dict):
            # If the value is a dictionary, recurse
            found_path = find_string_path(value, target, current_path)
            if found_path:  # If the path is found, return it
                return found_path
        elif isinstance(value, str) and re.search(target, value):
            # If the target regex is found in the string value, return the path
            return current_path

    return None  # If the target string is not found

#####################3



# for x in posts:
#     a=find_string_path(x, 'please')
#     print(a)




for obj in posts:
    
    try:    
          
          #parent_post_story
        
        #   print(obj['data']['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context'].keys())
          
          #print(obj['data']['node']['comet_sections']['content']['story']['comet_sections']['message']['story']['message']['text'])
        if 'node' in obj['data'].keys():
            base=obj['data']['node']

            data = {}
            for x in columns:
                data[x] = None
            #post1 
            if 'timeline_list_feed_units' in base.keys():

                try:
                    data['post_id']=base['timeline_list_feed_units']['edges'][0]['node']['post_id']
                except:
                    data['post_id']=''

                try: 
                   data['post_text']=base['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['content']['story']['message']['text'] 
                except:
                    data['post_text']='' 
                try:
                    data['post_creation_time']=base['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['context_layout']['story']['comet_sections']['metadata'][0]['story']['creation_time'] 
                except:
                    data['post_creation_time']=''
                    
                try:
                    data['post_url']=base['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['context_layout']['story']['comet_sections']['metadata'][0]['story']['url']
                except:
                    data['post_url']=''

                try:
                    data['attachment_text']=base['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['content']['story']['attached_story']['message']['text']
                except:
                    data['attachment_text']=''
                try:
                    data['attachment_names']=base['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['content']['story']['attached_story']['actors']['name']
                except:
                    data['attachment_names']=''
                try:
                    data['number_of_reactions']=base['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['feedback_target_with_context']['comet_ufi_summary_and_actions_renderer']['feedback']['reaction_count']['count']
                except:
                    data['number_of_reactions']=''
                try:
                    data['number_of_comments']=base['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['feedback_target_with_context']['comment_rendering_instance']['comments']['total_count']
                except:
                    data['number_of_comments']=''

                try:
                    data['comment_text']=base['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['body']['text']
                
                except:
                    data['comment_text']=''

                try:
                    data['comment_creation_time']=base['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['created_time']
                except: 
                    data['comment_creation_time']=''

                try:
                    data['comment_author']=base['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['author']['name']

                except:
                    data['comment_author']=''
                
                try:
                    data['comment_url']=base['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['comment_action_links'][0]['comment']['url']

                except:
                    data['comment_url']=''

                try:
                    data['reply_to_comment_text']=base['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['relevant_contextual_replies']['nodes'][0]['comment']['body']['text']
                except:
                    data['reply_to_comment_text']=''

                try:
                    data['reply_author_name']=base['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['relevant_contextual_replies']['nodes'][0]['comment']['author']['name']
                except:
                    data['reply_author_name']=''

                try:
                    data['comment_post_id']=base['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['feedback']['plugins'][0]['post_id']

                except:
                    data['comment_post_id']=''
               
              
            #post2
            else:

                try:
                    data['post_id']=base['post_id']
                except:
                    data['post_id']=''

                try: 
                   data['post_text']=base['comet_sections']['content']['story']['message']['text']
                except:
                    data['post_text']='' 
                try:
                    data['post_creation_time']=base['comet_sections']['context_layout']['story']['comet_sections']['metadata'][0]['story']['creation_time']
                except:
                    data['post_creation_time']=''
                    
                try:
                    data['post_url']=base['comet_sections']['context_layout']['story']['comet_sections']['metadata'][0]['story']['url']
                except:
                    data['post_url']=''

                try:
                    data['attachment_text']=base['comet_sections']['content']['story']['attached_story']['message']['text']
                except:
                    data['attachment_text']=''
                try:
                    data['attachment_names']=base['comet_sections']['content']['story']['attached_story']['actors'][0]['name']
                except:
                    data['attachment_names']=''
                try:
                    data['number_of_reactions']=base['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['feedback_target_with_context']['comet_ufi_summary_and_actions_renderer']['feedback']['reaction_count']['count']
                except:
                    data['number_of_reactions']=''
                try:
                    data['number_of_comments']=base['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['feedback_target_with_context']['comment_rendering_instance']['comments']['total_count']
                except:
                    data['number_of_comments']=''

                try:
                    data['comment_text']=base['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['body']['text']
                
                except:
                    data['comment_text']=''

                try:
                    data['comment_creation_time']=base['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['created_time']
                except: 
                    data['comment_creation_time']=''

                try:
                    data['comment_author']=base['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['user']['name']

                except:
                    data['comment_author']=''
                
                try:
                    data['comment_url']=base['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['comment_action_links'][0]['comment']['url']

                except:
                    data['comment_url']=''

                try:
                    data['reply_to_comment_text']=base['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['relevant_contextual_replies']['nodes'][0]['comment']['body']['text']
                except:
                    data['reply_to_comment_text']=''

                try:
                    data['reply_author_name']=base['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['relevant_contextual_replies']['nodes'][0]['comment']['user']['name']
                except:
                    data['reply_author_name']=''

                try:
                    data['comment_post_id']=base['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['interesting_top_level_comments'][0]['comment']['feedback']['plugins'][0]['post_id']

                except:
                    data['comment_post_id']=''
           

            count1+=1

            all_data.append(data)
        else: continue
    except:
        count+=1

print(count)
#print(count1)
import pandas as pd

df=pd.DataFrame(all_data)
print(df[['post_creation_time','comment_creation_time']].head(20))
df['post_creation_time'] = [int(x) if x != '' else None for x in df['post_creation_time']]
df['comment_creation_time'] = [int(x) if x != '' else None for x in df['comment_creation_time']]
df['post_creation_time'] = df['post_creation_time'].apply(lambda x: uni_to_normal(x) if pd.notna(x) else None)
df['comment_creation_time'] = df['comment_creation_time'].apply(lambda x: uni_to_normal(x) if pd.notna(x) else None)

print(df[['post_creation_time','comment_creation_time']].head(20))


df.to_csv('facebook_dataset.csv', index=False)
# print(df[['post_url','comment_text','post_text']].iloc[30])
# print(df[['post_url','comment_text','post_text']].iloc[30][1])
# print(df[['post_url','reply_to_comment_text','post_text']].iloc[30][1],'tuta')
# print(df['post_url'].iloc[30])
# for x in data:
#     if "https://www.facebook.com/api/graphql/" == x['request']['url']:
#         try:
#             response = x['response']['content']['text'].replace('\n', '')
            
#             json_objects = fix_json_structure(response)
#             json_objects = json.loads(json_objects)
            
#             content=content+response.replace('\\"','')+","


            
#             for obj in json_objects:
                
#                 if obj:  # Ensure the object is not empty
#                     #print(obj.keys())
#                     #print(obj.keys())
#                     print('-------------------')
#                     #print(obj['data']['node'].keys()) #id , timeline_list_feed_units
#                     #print(obj['data']['node']['timeline_list_feed_units']['edges'][0])
#                     #print(((obj['data']['node']['timeline_list_feed_units']['edges'][0]['node'])))#.keys())))
#                     #print(obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['content']['story']['attached_story']['message']['text'])
#                     #print('by:')
#                     print(obj['node'].keys())
#                     try:
                        
#                         if 'page_info' in obj['data'].keys():
#                             continue
                        
#                         if 'viewer' in obj['data'].keys():
#                             continue
                            
#                     except Exception as e:
#                         pass
#                     if 'cursor' in obj['data'].keys():
#                         #'need to correct this'
#                         #print((obj['data']))
#                         #print('asdasdasdas')
#                         pass
#                     #print(obj['data']['node'].keys())
                   
#                     if 'timeline_list_feed_units' in obj['data']['node'].keys():
#                         #already checked
#                         pass
#                     print(obj['data']['node'].keys())
#                     if 'attached_story' in obj['data']['node'].keys():
#                         #print(obj['data']['node'])
#                         pass
#                     #print((obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['comet_sections']['call_to_action']))#.keys()))#.keys()))#.keys())) #.keys()))#  ['name']))#.keys() ))#.keys()))
#                     print('-------------------')
#                     # count1+=1   
                    # if obj['data']['node']['timeline_list_feed_units']['edges'][0]['node']['__typename']=='Story':
                    #         data=str(obj['data']['node']['timeline_list_feed_units']['edges']).replace('\n', '')
                    #         check=re.search(message_pattern, data, re.DOTALL)
                    #         post=re.search(post_text_pattern, str(obj['data']['node']['timeline_list_feed_units']['edges']), re.DOTALL)
                    #         #print(post)
                    #         #print('post--------------------',post.group(1))
                    #         posts.append(post.group(1))
                    #         count+=1
                            #print(count)
                            #print(count1)
                           
                    # comment=re.search(comment_text_pattern, obj['data']['node']['timeline_list_feed_units']['edges'])
                    # print('post--------------------',post)
                    # print('comment--------------------',comment)
                    #if 'label' in obj.keys():
                        #print(obj['data'].keys())
                    # print(obj['data'].keys())
                    # if 'node' in obj['data']:
                    #     node = obj['data']['node']
                    #     print(node.keys())
                    #     print('-------------------')
                    
                    
#         except Exception as e:
#             #pass
#             count3+=1
            
#             #print('Error:', e)
# print(count3)
#print(count,'da')
# for x in posts[:20]:
#     print(x)
#     print('-------------------')