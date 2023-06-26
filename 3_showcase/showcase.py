import pandas as pd

df_deputies = pd.read_csv('../0_datasets/integrated_data/df_deputies.csv', index_col = 0)
df_sessions = pd.read_csv('../0_datasets/integrated_data/df_sessions.csv', index_col = 0)
df_events = pd.read_csv('../0_datasets/integrated_data/df_events.csv', index_col = 0)
df_speeches = pd.read_csv('../0_datasets/integrated_data/df_speeches.csv', index_col = 0).fillna(-1).astype(int)
dl_deputy_period = pd.read_csv('../0_datasets/integrated_data/dl_deputy_period.csv')
dl_session_deputy = pd.read_csv('../0_datasets/integrated_data/dl_session_deputy.csv')
dl_deputy_event = pd.read_csv('../0_datasets/integrated_data/dl_deputy_event.csv')
dl_party_event = pd.read_csv('../0_datasets/integrated_data/dl_party_event.csv')

# Get only deputies of 19th election period:
df_deputies_19 = df_deputies.filter(items=dl_deputy_period[dl_deputy_period['election_period'] == 19]['deputy_id'], axis = 0)


def count_party_events_per_deputy(deputies, events,speeches, party_event, session_deputy, event_type):
    df_a = events.merge(party_event, left_index=True, right_on='event_id')
    df_a = df_a[df_a['event_type'] == event_type]  # count claps
    df_b = df_a.merge(speeches, left_on = 'speech_id', right_index=True)[['party_id','session_id']]
    df_c = deputies.merge(session_deputy, left_index=True, right_on='deputy_id')[['deputy_id', 'fraktion', 'session_id']]
    df_d = df_c.merge(df_b, left_on=['fraktion', 'session_id'], right_on=['party_id', 'session_id'])
    result = df_d['deputy_id'].value_counts()
    return result


def count_personal_events(events, deputy_event, event_type):
    df_a = events.merge(deputy_event, left_index=True, right_on='event_id')
    df_a = df_a[df_a['event_type'] == event_type]  # count claps
    result = df_a['deputy_id'].value_counts()
    return result


def count_personal_events_at_other_party_speaker(speeches, deputies, events, deputy_event, event_type):
    df_a = speeches.merge(deputies, left_on='speaker_id', right_index = True)[['speaker_id', 'fraktion', 'session_id']].rename(columns = {'fraktion':'speaker_party'})
    df_b = events.merge(df_a, left_on='speech_id', right_index=True)
    df_b = df_b.merge(deputy_event, left_index=True, right_on='event_id')
    df_b = df_b[df_b['event_type'] == 2]
    df_c = df_b.merge(deputies[['fraktion']], left_on='deputy_id', right_index=True)
    df_c = df_c[df_c['fraktion'] != df_c['speaker_party']]
    result = df_c['deputy_id'].value_counts()
    return result


def count_party_events_per_party(events, event_party, event_type):
    df_a = events.merge(event_party, left_index=True, right_on='event_id')
    if event_type is not None:
        df_a = df_a[df_a['event_type'] == event_type]
    result = df_a['party_id'].value_counts()
    return result


event_types = ['Beifall', 'Zwischenruf', 'Lachen', 'Zuruf', 'Widerspruch', 'Heiterkeit']
for i in range(len(event_types)):
    df_deputies_19[f'party_{event_types[i]}_count'] = df_deputies_19.index.map(
        count_party_events_per_deputy(df_deputies_19, df_events,df_speeches,dl_party_event,dl_session_deputy, i)
    ).fillna(0).astype(int)

    df_deputies_19[f'person_{event_types[i]}_count'] = df_deputies_19.index.map(
        count_personal_events(df_events, dl_deputy_event, i)
    ).fillna(0).astype(int)

    df_deputies_19[f'total_{event_types[i]}_count'] = df_deputies_19[f'person_{event_types[i]}_count'] + df_deputies_19[f'party_{event_types[i]}_count']

    df_deputies_19[f'person_{event_types[i]}_count_other_party_speaker'] = df_deputies_19.index.map(
        count_personal_events_at_other_party_speaker(df_speeches, df_deputies, df_events, dl_deputy_event, i)
    ).fillna(0).astype(int)

    print(f'{event_types[i]}:')
    print(count_party_events_per_party(df_events, dl_party_event, i))
    

df_deputies_19.to_csv('../3_showcase/df_result.csv', index=True)
# --------------------------------------------------
