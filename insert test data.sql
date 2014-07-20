INSERT INTO network_outerpoint (id, lat, lng, description, name) VALUES (1, 55.937134, 37.514661, 'Офис под крышей на Гостиничной', 'iDa Mobile');

INSERT INTO network_object (id, name, description, description_far, description_near, description_immediate, outer_point_id) VALUES (1, 'Стол Кирилла', 'Стол Кирилла в офисе на крыше', 'ДАЛЕКО от стола Кирилла', 'БЛИЗКО от стола Кирилла', 'НА столе Кирилла', 1);
INSERT INTO network_object (id, name, description, description_far, description_near, description_immediate, outer_point_id) VALUES (2, 'Холодильник', 'Холодильник в офисе на крыше', 'ДАЛЕКО от холодильника', 'Близко от холодильника', 'НА холодильнике', 1);
INSERT INTO network_object (id, name, description, description_far, description_near, description_immediate, outer_point_id) VALUES (3, 'Окно в конце коридора', 'Окно в конце коридора в офисе на крыше', 'ДАЛЕКО от окна в конце коридора', 'БЛИЗКО от окна в конце коридора', 'СОВСЕМ РЯДОМ с окном в конце коридора', 1);

INSERT INTO network_innerpoint (id, x, y, floor_number, description, related_object_id) VALUES (1, 0, 2, 0, 'Стол Кирилла', 1);
INSERT INTO network_innerpoint (id, x, y, floor_number, description, related_object_id) VALUES (2, -3, 0, 0, 'Холодильник', 2);
INSERT INTO network_innerpoint (id, x, y, floor_number, description, related_object_id) VALUES (3, 2, -10, 0, 'Окно в конце коридора', 3);

INSERT INTO network_beacon (id, uuid, major, minor, frequency, description, inner_point_id) VALUES (1, 'f7826da6-4fa2-4e98-8024-bc5b71e0893e', 64955, 17705, null, 'XG5x', 1);
INSERT INTO network_beacon (id, uuid, major, minor, frequency, description, inner_point_id) VALUES (2, 'f7826da6-4fa2-4e98-8024-bc5b71e0893e', 4659, 12780, null, 'bedV', 2);
INSERT INTO network_beacon (id, uuid, major, minor, frequency, description, inner_point_id) VALUES (3, 'f7826da6-4fa2-4e98-8024-bc5b71e0893e', 48806, 34109, null, 'SB48', 3);
INSERT INTO network_beacon (id, uuid, major, minor, frequency, description) VALUES (4, 'f7826da6-4fa2-4e98-8024-bc5b71e0893e', 11605, 2932, null, 'B4tX');
INSERT INTO network_beacon (id, uuid, major, minor, frequency, description) VALUES (5, 'f7826da6-4fa2-4e98-8024-bc5b71e0893e', 50069, 12003, null, 'pNPE');

INSERT INTO network_person (id, first_name, middle_name, last_name, twitter_account, description) VALUES (1, 'Кирилл', 'Андреевич', 'Осипов', '', 'Ведущий iOS девелопер в iDa Mobile');
INSERT INTO network_person (id, first_name, middle_name, last_name, twitter_account, description) VALUES (2, 'Сергей', '', 'Рябов', '@colriot', 'Ninja developer');


INSERT INTO network_category (id, description, name) VALUES (1, 'Android develoment feed', 'Android Dev');
INSERT INTO network_category (id, description, name) VALUES (2, 'iOS development feed', 'iOS Dev');
INSERT INTO network_category (id, description, name) VALUES (3, 'Фуршет', 'Party');


INSERT INTO network_event (id, time_start, time_finish, category_id, object_id, description) VALUES (1, '2014-07-16 14:00:00', '2014-07-16 14:15:00', 2, 1, 'Приветственное слово от Кирилла Осипова за его столом');
INSERT INTO network_event (id, time_start, time_finish, category_id, object_id, description) VALUES (2, '2014-07-16 14:15:00', '2014-07-16 14:45:00', 2, 1, 'Продолжение выступления великого оратора');
INSERT INTO network_event (id, time_start, time_finish, category_id, object_id, description) VALUES (3, '2014-07-16 14:00:00', '2014-07-16 14:15:00', 1, 3, 'Около окна лучший в мире прогер Сергей Рябов поведает нам о себе');
INSERT INTO network_event (id, time_start, time_finish, category_id, object_id, description) VALUES (4, '2014-07-17 00:00:00', '2014-07-17 02:00:00', 1, 3, 'Заключительно слово Сергея');
INSERT INTO network_event (id, time_start, time_finish, category_id, object_id, description) VALUES (5, '2014-07-16 17:00:00', '2014-07-16 18:00:00', 3, 2, 'Самый лучший в мире фуршет от Дмитрия Феофанова');


INSERT INTO network_event_speaker (id, event_id, person_id) VALUES (1, 1, 1);
INSERT INTO network_event_speaker (id, event_id, person_id) VALUES (2, 2, 1);
INSERT INTO network_event_speaker (id, event_id, person_id) VALUES (3, 3, 2);
INSERT INTO network_event_speaker (id, event_id, person_id) VALUES (4, 4, 2);
